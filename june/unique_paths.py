import math
class Solution:
    """#62. A robot is located at the top-left corner of a m x n grid.

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid.

    How many possible unique paths are there?
    """
    def uniquePaths(self, m: int, n: int) -> int:
        total = m+n-2
        result = 1
        for i in range(total, m-1, -1): result *= i
        return int(result / math.factorial(n-1))
