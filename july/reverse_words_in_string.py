class Solution:
    """#151. Given an input string, reverse the string word by word."""
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])
