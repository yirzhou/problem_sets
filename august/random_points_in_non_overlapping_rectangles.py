import bisect, itertools, random
class Solution:
    """#497. Given a list of non-overlapping axis-aligned rectangles rects, 
    write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.
    """
    def __init__(self, rects):
        w = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(w) for i in itertools.accumulate(w)]
        self.rects = rects

    def pick(self):
        n_rect = bisect.bisect(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[n_rect] 
        return [random.randint(x1, x2),random.randint(y1, y2)]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
