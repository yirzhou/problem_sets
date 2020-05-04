import math

class Solution:
    """Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation."""
    def find_complement(self, num: int) -> int:
        power = math.floor(math.log2(num))
        if num>=2**power: power+=1
        return 2**power-1-num
