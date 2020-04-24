from collections import deque, OrderedDict

class LRUCache:
    '''The first solution is not the most optimal one.
    The main idea is to put the newest/youngest items to the
    back of the queue. When the size reaches the threshold, 
    the leftmost items will be popped off the queue. 
    Worst case (<key, age>):
    <A,1>, <B,2>, <C,3>, <C,4>, <C,5>, <B,6>, <B,7>...
    and then, say a new item is inserted and the cache is full,
    <A,1> is the oldest which gets popped off.
    Then, another item is added, and in theory C should be popped off.
    However, it requires a lot of popleft() calls to finally remove C.
    '''

    def __init__(self, capacity):
        self.current_age = 0
        self.store = {}
        self.ages = {}
        self.thresh = capacity
        self.size = 0
        self.queue = deque()
        

    def get(self, key): 
        if key in self.store:
            self.current_age += 1
            self.ages[key] = self.current_age
            self.queue.append((key, self.current_age))
            return self.store[key]
        return -1 

    def put(self, key, value):
        self.current_age += 1

        if key not in self.store:
            if self.size == self.thresh:
                (oldest_key, age) = self.queue.popleft()
                while oldest_key not in self.store or self.ages[oldest_key] != age: (oldest_key, age) = self.queue.popleft()
                del self.ages[oldest_key]
                del self.store[oldest_key]
            else: self.size += 1

        self.store[key] = value
        self.ages[key] = self.current_age
        self.queue.append((key, self.current_age))

class LRU:
    '''This version utilizes the OrderedDict,
    which is a much more efficient way of manipulating
    the linked structure. It is essentially the equivalent
    of the LinkedHashMap in Java.
    '''
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.store = OrderedDict()

    def get(self, key):
        if key in self.store:
            self.store.move_to_end(key)
            return self.store[key]
        return -1

    def put(self, key, value):
        if key not in self.store:
            if self.size < self.capacity: self.size += 1
            else: self.store.popitem(last=False)
        else: self.store.move_to_end(key)
        self.store[key] = value
        
cache = LRUCache( 2 )

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)     
cache.put(3, 3)    
cache.get(2);       
cache.put(4, 4)
cache.get(1)    
cache.get(3)
cache.get(4)      
