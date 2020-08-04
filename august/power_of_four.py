from math import log
class Solution:
    """#342. Given an integer (signed 32 bits), write a function to check whether it is a power of 4."""
    def isPowerOfFour(self, num: int) -> bool:
        return False if num <= 0 else int(log(num, 4)) == log(num, 4)
    