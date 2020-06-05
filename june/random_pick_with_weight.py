import random
class Solution:
    """#528. Given an array w of positive integers, 
    where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
    """
    def __init__(self, w):
        self.length = len(w)
        self.w = w
        for i in range(1, self.length):
            self.w[i] += self.w[i-1]
        self.top = self.w[-1]

    def pickIndex(self):
        """Binary search approach.
        """
        rand = random.randint(1,self.top)
        lo, hi = 0, self.length-1
        while lo < hi:
            mid = lo+(hi-lo)//2
            if rand<= self.w[mid]: hi = mid
            else: lo = mid+1
        return lo

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()