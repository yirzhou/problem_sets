class Solution:
    '''Given two strings text1 and text2, return the length of their longest common subsequence.
    A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted 
    without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
    A common subsequence of two strings is a subsequence that is common to both strings.
    '''
    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        '''This is similar to the knapsack problem.
        Note the way of allocating a multi-dimensional list:
        - dp = [[0 for col in range(len(text2)+1)] for row in range(len(text1)+1)]
        1. Time: O(m*n), where m and n are the lengths of strings
        2. Space: O(m*n)
        '''
        n,m=len(text1),len(text2)
        dp = [[0 for col in range(len(text2)+1)] for row in range(len(text1)+1)]
        for i, c in enumerate(text1):
            for j, d in enumerate(text2):
                dp[i + 1][j + 1] = 1 + dp[i][j] if c == d else max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]

print(Solution().longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
