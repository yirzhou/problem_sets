class Solution:
    """#438:
    Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
    """
    def findAnagrams(self, s: str, p: str):
        """Sliding-window technique:
        - Time: O(N)
        - Space: O(N)
        """
        counts = {}
        s_len, p_len = len(s), len(p)
        for letter in p:
            if letter not in counts: counts[letter] = 0
            counts[letter] += 1
        count = len(counts)
        
        results = []
        lo, hi = 0, 0
        
        while hi < s_len:
            if s[hi] in counts:
                counts[s[hi]] -= 1
                if counts[s[hi]] == 0: count -= 1
                    
            while count == 0:
                if hi-lo+1 == p_len: 
                    results.append(lo)
                start_char = s[lo]
                if start_char in counts:
                    counts[start_char] += 1
                    if counts[start_char] > 0: count += 1
                lo += 1
            hi += 1
        return results
    