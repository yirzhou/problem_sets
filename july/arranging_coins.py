class Solution:
    """#441. You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

    Given n, find the total number of full staircase rows that can be formed.

    n is a non-negative integer and fits within the range of a 32-bit signed integer.
    """
    def arrangeCoins(self, n: int) -> int:
        level = 0
        num = 0
        
        while n > 0:
            num += 1
            n -= num
            level += 1
        return level - 1 if n < 0 else level
