class Solution:
    """#190. Reverse bits of a given 32 bits unsigned integer."""
    def reverseBits(self, n: int) -> int:
        n_bin = bin(n).split('b')[-1]
        n_bin = '0'*(32-len(n_bin))+n_bin
        return int(n_bin[::-1], 2)
        