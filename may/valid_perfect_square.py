class Solution:
    """Given a positive integer num, write a function which returns True if num is a perfect square else False"""
    def is_perfect_square(self, num: int) -> bool:
        """Solution using binary search.
        - Time: O(lg(N))
        - Space: O(1)
        """
        if num == 1: return True
        
        begin, end = 1, num
        while begin <= end:
            mid = begin + (end-begin)//2
            sq = mid**2
            if sq == num: return True
            elif sq > num: end = mid-1
            else: begin = mid+1
        return False