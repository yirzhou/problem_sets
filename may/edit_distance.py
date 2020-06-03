class Solution:
    """#72. Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
    You have the following 3 operations permitted on a word:
    1. Insert a character
    2. Delete a character
    3. Replace a character
    """
    def minDistance(self, word1: str, word2: str) -> int:
        """DP Approach: with word1[0:i] and word2[0:j]:
        - if word1[i] == word2[j], dp[i][j] = dp[i-1]dp[j-1]
        - else:
            1. replace a letter: dp[i][j] = dp[i-1][j-1]+1
            2. delete a letter: dp[i][j] = dp[i][j-1] + 1
            3. add a letter: dp[i][j] = dp[i-1][j] + 1
            Then, find the minimum of those three.

        - Space: O(M*N)
        - Time: O(M*N)
        """
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1): 
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j
            for k in range(1, m+1):
                if word1[k-1] == word2[j-1]:
                    dp[k][j] = dp[k-1][j-1]
                else:
                    dp[k][j] = min(dp[k-1][j-1]+1, dp[k][j-1]+1, dp[k-1][j]+1)
        return dp[m][n]
    