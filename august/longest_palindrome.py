class Solution:
    """#409. Given a string which consists of lowercase or uppercase letters, 
    find the length of the longest palindromes that can be built with those letters.

    This is case sensitive, for example "Aa" is not considered a palindrome here.

    Note:
    Assume the length of given string will not exceed 1,010.
    """
    def longestPalindrome(self, s: str) -> int:
        counter = {}
        
        for char in s:
            if char not in counter: counter[char] = 0
            counter[char] += 1
        
        odd, length = 0, 0
        
        for val in counter.values():
            even = (val//2)*2
            if even != val: odd = 1
            length += even
        
        if odd: length += 1
        return length 
