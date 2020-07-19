class Solution:
    """#67. Given two binary strings, return their sum (also a binary string).

    The input strings are both non-empty and contains only characters 1 or 0.
    """
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2)+int(b, 2)).split('b')[-1]
