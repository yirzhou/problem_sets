class Solution:
    """Write a function to crush candy in one dimensional board. 
    In candy crushing games, groups of like items are removed from the board. 
    In this problem, any sequence of 3 or more like items should be removed and 
    any items adjacent to that sequence should now be considered adjacent to each other. 
    This process should be repeated as many time as possible. 
    You should greedily remove characters from left to right."""
    def candy_crush(self, s):
        last = len(s)-1
        lo, hi = 0, 0
        while hi <= last:
            char = s[lo]
            if s[hi] != char:
                if hi - lo >= 3:
                    s = self.crush(lo, hi, s)
                    last = len(s)-1
                    lo, hi = 0, 0
                else: lo = hi
            hi += 1
        return s
    
    def crush(self, lo, hi, s):
        s_list = []
        for i in range(lo):
            s_list.append(s[i])
        for i in range(hi, len(s)):
            s_list.append(s[i])
        return ''.join(s_list)
    
sol = Solution()
print(sol.candy_crush("aabbbacd"))
