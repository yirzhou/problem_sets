import math
class Solution:
    """#338. Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array."""
    def countBits(self, num: int):
        """For every number, #bits = 1 + num-2**(math.floor(math.log2(n)))
        - Time: O(N)
        - Space: O(N)
        """
        bits = [0]*(num+1)
        for n in range(1, num+1):
            bits[n] += (1 + bits[n - 2**(math.floor(math.log2(n)))])
        return bits
        