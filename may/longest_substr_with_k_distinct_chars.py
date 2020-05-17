class Solution:
    """#159. Longest Substring with At Most Two Distinct Characters"""
    def length_of_longest_substr_k_distinct(self, s, K):
        counts = {}
        begin, end = 0, 0
        count = 0
        
        s_len = len(s)
        max_len = 0

        while end < s_len:
            current = s[end]    
            if current not in counts: counts[current] = 0
            counts[current] += 1
            if counts[current] == 1: count += 1
            
            if count <= K:
                max_len = max(max_len, end-begin+1)
            else:
                while count > K:
                    begin_char = s[begin]
                    counts[begin_char] -= 1
                    if counts[begin_char] == 0: count -= 1
                    begin += 1
            end += 1
        
        return max_len
        
sol = Solution()
print(sol.length_of_longest_substr_k_distinct("aabbcd", 3))
