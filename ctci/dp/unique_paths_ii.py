class Solution:
    """LC #63:
    A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

    Now consider if some obstacles are added to the grids. How many unique paths would there be?
    """
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        rows, cols = len(grid), len(grid[0])
        memo = dict()
        return self.unique_path(grid, 0, 0, memo)

    def unique_path_dp(self, grid):
        """Dynamic programming approach:
        Starting from the destination, exploring row by row.
        dp[row][col] = dp[row+1][col] + dp[row][col+1]

        - Time: O(N^2)
        - Space: O(N^2)
        """
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]
        dp[rows-1][cols-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if grid[r][c]: dp[r][c] = 0
                else:
                    if not(r == rows-1 and c == cols-1): dp[r][c] = dp[r+1][c]+dp[r][c+1]
        
        return dp[0][0]  
        
    def unique_path(self, grid, row, col, memo):
        """Memoization approach:
        - Time: O(N^2)
        - Space: O(N^2)
        """
        if (not self.is_valid(grid, row, col)) or grid[row][col] == 1: return 0
    
        if row == len(grid)-1 and col == len(grid[0])-1: return 1
        else: 
            down, right = 0, 0
            if memo.get((row+1, col), None): down = memo[(row+1, col)]
            else: down = self.unique_path(grid, row+1, col, memo)
                
            if memo.get((row, col+1), None): right = memo[(row,col+1)]
            else: right = self.unique_path(grid, row, col+1, memo)
            
            memo[(row,col)] = down+right
            return memo[(row,col)]
  
    def is_valid(self, grid, row, col):
        return False if row > len(grid)-1 or col > len(grid[0])-1 else True
        