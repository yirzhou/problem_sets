import math
class Solution:
    """#279. Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n."""
    def numSquares(self, n: int) -> int:
        if self.is_square(n):
            return 1
        
        while n&3 == 0:
            n >>= 2
            
        if n&7 == 7:
            return 4
        
        sqrt_n = int(math.sqrt(n))
        for i in range(1, sqrt_n + 1):
            if self.is_square(n - i*i):
                return 2
        return 3
        
    def is_square(self, n):
        sqrt_n = int(math.sqrt(n))
        return sqrt_n*sqrt_n == n
