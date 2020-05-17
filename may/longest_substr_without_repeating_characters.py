
class Solution:
    """#3. Longest Substring Without Repeating Characters:
    Given a string, find the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Linear-time approach. A variant of sliding-window.
        - Time: O(N)
        - Space: O(N)
        """
        indices = {}
        begin, end = 0, 0
        
        length = len(s)
        max_len = 0
        
        while end < length:
            char = s[end]
            
            if char not in indices or (char in indices and indices[char] < begin):
                indices[char] = end
                max_len = max(max_len, end-begin+1)
            else:
                begin = indices[char]+1
                indices[char] = end
            end += 1
        return max_len
