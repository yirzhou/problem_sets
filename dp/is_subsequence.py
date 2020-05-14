class Solution:
    """LC #392: Given a string s and a string t, check if s is subsequence of t."""
    def is_subsequence(self, s: str, t: str) -> bool:
        """
        - Time: O(N)
        - Space: O(1)
        """
        cur_idx = 0
        end = len(s)-1
        if end == -1: return True
        
        for char in t:
            if char == s[cur_idx]: cur_idx += 1
            if cur_idx == end+1: return True
        return False
        