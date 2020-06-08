class Solution:
    """#231. Given an integer, write a function to determine if it is a power of two."""
    def isPowerOfTwo(self, n: int) -> bool:
        return (n != 0) and ((n & (n - 1)) == 0)
