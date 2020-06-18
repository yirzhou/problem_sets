class Solution:
    """#275. Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, 
    write a function to compute the researcher's h-index.
    """
    def hIndex(self, citations):
        lo, hi = 0, len(citations)-1
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if citations[mid] >= len(citations)-mid: hi = mid-1
            else: lo = mid+1
            
        return len(citations)-lo
