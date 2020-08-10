class Solution:
    """#171. Given a column title as appear in an Excel sheet, return its corresponding column number."""
    def titleToNumber(self, s: str) -> int:
        start_char = len(s) - 1
        result = 0
        for char in s:
            result += (ord(char) - 64) * (26**start_char)
            start_char -= 1
        return result
    