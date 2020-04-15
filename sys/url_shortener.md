# URL Shortener

## Steps
### 1. Ask questions
**Is this a full web app with a interface?**: It's just an API
**Should we let people *choose* their shortlinks?**: Yes.

### 2. Design Goals
1. should be able to store a *lot of* links.
2. shortlinks should be as short as possible.
3. following a shortlinks should be fast.
4. shortlink follower should be resillient to load spikes (could be the top story on Reddit, for example).


### 3. Data Model
```
ShortLink
- slug
- destination
```

### 4. Code Sketch

**First, lets use REST API**, such as something like `ca.ke/api/v1/shortlink`.
Some pseudocode like the following:
```python
def shortlink(request):
    if request['method'] is not 'POST':
        return Response(501)  # HTTP 501 NOT IMPLEMENTED

    destination = request['data']['destination']
    if 'slug' in request['data']:
        # If they included a slug, use that
        slug = request['data']['slug']
    else:
        # Else, make them one
        slug = generate_random_slug()

    DB.insert({'slug': slug, 'destination': destination})

    response_body = { 'slug': slug }
    return Response(200, json.dumps(response_body))  # HTTP 200 OK
```

**Second, let's make a way to follow a ShortLink** (format will be `ca.ke/$slug`).
```
Here comes a potential issue: we want to reserve some paths for ourselves. For example, we might have an "about" page using a slug "about" for our own website, so it should not be generated for the use for any user. Potential solution could be that we can append something in front of it to distinguish it from the user one: "ca.ke/w/about".
```
Then, the code for redirection endpoint:
```python
def redirect(request):
    destination = DB.get({'slug': request['path']})['destination']
    return Response(302, destination)
```

**Next, slug generation!**
We have the previous requirements:
1. need to store a lot of links.
2. should be as short as possible.

The length is crucial here: if we have `c` characters in the shortlink, it can have `c^n` different combinations.

**What characters can we allow in our randomly-generated slugs?** `RFC` has this all layed out for us. 

**How many distinct slugs do we need?** Say, we generate 100,000 slugs per minute, for the period of 100 years. That's about 145 million new links a day, 52.5 billion a year, and 5.2 trillion slugs for 100 years. 

**How short can we make our slugs while still getting enough distinct possibilities?** Say we have 72 allowed characters (numbers, letters, some special characters), and solve for `n` in `72^n = 5.2 trillion`. `n` is roughly 7 characters. 

**How do we generate a random slug? Use base conversion!**
The following code essentially keep track of a global random slug id that gets incremented when a new slug is randomly generated. The ID will be mapped to a base-64 alphanumerical system. 
```python
def generate_random_slug():
    global current_random_slug_id
    slug = base_conversion(current_random_slug_id, base_62_alphabet)
    current_random_slug_id += 1
    return slug
```

For example, if our ID is 7,912, and we have the following mapping:
```
0: 0,
1: 1,
2: 2,
3: 3,
...
10: a,
11: b,
12: c,
...
36: A,
37: B,
38: C,
...
61: Z
```
7,912 will be "2 3 38" (three-digit) in base-62, which gives us `23C`. We are also able to convert a shortlink back to its base-10 form as well - just reverse the process.

If the `current_random_slug_id` is less than 7-digit in base-62, just pad the rest digits with zeros and we will be gold. Also, we have to check if a user-generated slug has already been used:
```python
def generate_random_slug():
    global current_random_slug_id
    while True:
        slug = base_conversion(current_random_slug_id, base_62_alphabet)
        current_random_slug_id += 1
        # Make sure the slug isn't already used
        existing = DB.get({'slug': slug})
        if not existing:
            return slug
```

Now, looking back at the third and fourth of the goals:
- Following a shortlink should be fast.
- The shortlink follower should be resilient to load spikes.

Since we do not care about relations in this case, we will go with a `NoSQL` database. How do we un-bottleneck database reads? The first step is to *make sure we're indexing the right way*. The obvious choise is to make the key for each row in the `ShortLink` table be *the slug*. 

**How else can we speed up database reads?** We could put as much of the data *in memory* as possible. However, depending on the DBMS, it could have already had a caching layer so we might not want to add extra complexity. If we *did* add a caching layer, we need to talk about:
1. Eviction strategy: LRU is the most common answer.
2. Sharding strategy: We can use more machines, but how do we decide which things go on which shard? The common answer is a "hash and mod strategy" - hash the key, mod the result by the number of shards, and you get a shard number to send your request to. But then how do you add or remove a shard without causing an unmanageable spike in cache misses? 

We could also shard our database instead of, or in addition to caching. This allows both reads and writes to be distributed across multiple machines. But, sharding of databases has the same challenges, and it makes joins very difficult if not impossible to do. 

Okay, now our redirects should go pretty quick, and should be resilient to load spikes. We have a solid system that fits all of our design goals!

1. We can store a lot of links.
2. Our shortlinks are as short as possible.
3. Following a shortlink is fast.
4. The shortlink follower is resilient to load spikes.

## Bonus
As with all system design questions, there are a bunch more directions to go into with this one. A few ideas:

1. At some point we'd probably want to consider splitting our link creation endpoint across multiple workers as well. This adds some complexity: how do they stay in sync about what the current_random_slug_id is?
```
Perhaps we could use some locking system. For example, in a task where the global ID is about to be written or modified, no one else can access it. 
```
2. Uptime and "single point of failure" (SPOF) are common concerns in system design. Are there any SPOFs in our current architecture? How can we ensure that an individual machine failure won't bring down our whole system?
3. Analytics. What if we wanted to show users some analytics about the links they've created? What analytics could we show, and how would we store and display them?
4. Editing and deleting. How would we add edit and delete features?
5. Optimizing for implementation time. We built something optimized for scale. How would our system design be different if we were just trying to get an MVP off the ground as quickly as possible?
