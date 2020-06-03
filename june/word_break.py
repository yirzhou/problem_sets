class Solution:
    """#139. Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
    determine if s can be segmented into a space-separated sequence of one or more dictionary words."""
    def wordBreak(self, s, wordDict):
        """DP approach:
        The idea is to slice the string into two pieces.
        For i, j, I check if s[:i] and s[i:j+1] both exists in the dictionary.
        Then, dp[j+1] will be marked true and it represents that s[:j+1] is in the dictionary.
        - Time: O(N^2)
        - Space: O(N)
        """
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i:j+1] in wordDict: dp[j+1] = True
                    if dp[-1]: return True
                    
        return dp[-1]
        