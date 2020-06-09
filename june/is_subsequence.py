class Solution:
    """#392. Given a string s and a string t, check if s is subsequence of t."""
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr, target = 0, len(s)
        
        for idx, letter in enumerate(t):
            if ptr == target: break
            if s[ptr] == letter:
                ptr += 1
        if ptr == target:
            return True
        return False
