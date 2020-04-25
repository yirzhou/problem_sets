# A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.
If an egg is dropped from above that floor, it will break. If it is dropped from that floor or below, it will be completely undamaged and you can drop the egg again.

Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.

## Breakdown
We could skip 10 floors each time. The worst case would again be floor 98 or 99, but we'd only drop the first egg 10 times and the second egg 9 times, for a total of 19 drops!

The worst case total number of drops increases by one each time the first egg *doesn't break*. Therefore, I could potentially compensate this increasing by one by skipping one floor less: ie. If I skip 10 floors the first time, I'd skip 9 floors the second time, and so on.

Hence, to decrease the number of floors we skip by one every time we move up, and to minimize the number of floors we skip the first time, we want to end up skipping just one floor at the very top:

<p align="center"><i>n+(n−1)+(n−2)+…+1=100</i></p>

which is a triangular series, and solving for n:
<p align="center"><i>n = 13.651</i></p>
Therefore, the first time I'd skip 14 floors, the second time I'd skip 13 floors, and so on.

**Worst cases:**
1. The breakpoint is the 13th floor, which takes 14 drops in total
2. The break point is the 98th floor: 14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 96, 97, 98, which takes 14 drops in total.

## What I've learned

This is one of our most contentious questions. Some people say, "Ugh, this is useless as an interview question," while others say, "We ask this at my company, it works great."

The bottom line is some companies do ask questions like this, so it's worth being prepared. There are a bunch of these not-exactly-programming interview questions that lean on math and logic. There are some famous ones about shuffling cards and rolling dice. If math isn't your strong suit, don't fret. It only takes a few practice problems to get the hang of these.
