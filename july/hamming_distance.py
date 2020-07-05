class Solution:
    """#461. Given two integers x and y, calculate the Hamming distance."""
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y 
        set_bits = 0

        while (n > 0) : 
            set_bits += n & 1
            n >>= 1

        return set_bits  
