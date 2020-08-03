class Solution:
    """#125. Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

    Note: For the purpose of this problem, we define empty string as valid palindrome.
    """
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            while not self.check(s[i]) and i < j: i+=1
            while not self.check(s[j]) and i < j: j-=1
            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1
        return True
            
    def check(self, char):
        code = ord(char)
        return 48 <= code <= 57 or 65 <= code <= 90 or 97 <= code <= 122
    