class Solution:
    """#1035. We write the integers of A and B (in the order they are given) on two separate horizontal lines.
    Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

    - A[i] == B[j];
    - The line we draw does not intersect any other connecting (non-horizontal) line.
    Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.
    Return the maximum number of connecting lines we can draw in this way.
    """
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """DP Approach:
        - Time: O(mn)
        - Space: O(mn)
        """
        m, n = len(A), len(B)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)] 
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = max(dp[i][j], 1+dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
        
    def memoized(self, A, B, i, j, memo):
        """Memoized solution.
        - Time: O(2^max(m,n))
        - Space: O(mn)
        """
        if i >= len(A) or j >= len(B):
            return 0
        if (i,j) in memo: 
            return memo[(i,j)]  
        if A[i] == B[j]:
            memo[(i, j)] = 1 + self.memoized(A, B, i+1, j+1, memo)
        else:
            memo[(i, j)] = max(self.memoized(A, B, i+1, j, memo), self.memoized(A, B, i, j+1, memo))
        return memo[(i, j)]
        