import math

class Solution:

    def brute_force(self, matrix) -> int:
        '''The suboptimal solution uses recursion and memoization.
        It basically walks through a line diagonally and returns the final maximum dimension.
        - Time: O((mn)^2)
        - Space: O(mn)
        '''
        # m is the height, n is the width
        if len(matrix) == 0: return 0
        m, n = len(matrix), len(matrix[0])
        memo = [[0 for _ in range(n)] for _ in range(m)]
        max_dimension = 0
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == '1': 
                    # max_dimension = max(max_dimension, self.__dfs(matrix, row, col, memo, 0))
                    max_dimension = max(max_dimension, self.__dfs(matrix, row, col, memo, 0))
        return max_dimension**2
        
    # def __dfs(self, matrix, m, n, visited, dimension):
    def __dfs(self, matrix, m, n, memo, dimension):
        if m>len(matrix)-1 or n > len(matrix[0])-1 or m < 0 or n < 0: return dimension
        
        if matrix[m][n] == '0': return dimension
        
        if memo[m][n] < dimension+1: 
            d = 1
            for num in range(dimension):
                if m-num-1 > -1 and n-num-1 > -1 and matrix[m-num-1][n] == '1' and matrix[m][n-num-1] == '1': d += 1
                else: 
                    memo[m][n] = d
                    return dimension

            memo[m][n] = max(memo[m][n], d)
        return self.__dfs(matrix, m+1, n+1, memo, dimension+1)

    def maximal_square(self, matrix) -> int:
        '''The optimal solution.
        It is yet again another knapsack-like problem that
        builds in a bottom-up fashion. 
        It keeps making sure that each '1' plus the '1's surrounding
        it can keep forming a square of a perticular dimension.

        - Time: O(mn)
        - Space: O(mn)
        '''
        # m is the height, n is the width
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        memo = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_dimension = 0
        for row in range(1, m+1):
            for col in range(1, n+1):
                if matrix[row-1][col-1] == '1': 
                    memo[row][col] = min(memo[row-1][col-1], memo[row][col-1], memo[row-1][col]) + 1
                    max_dimension = max(max_dimension, memo[row][col])
        return max_dimension**2
