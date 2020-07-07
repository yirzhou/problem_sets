class Solution:
    """#463. You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

    Grid cells are connected horizontally/vertically (not diagonally). 

    The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
    """
    def __init__(self):
        self.perimeter = 0
        
    def islandPerimeter(self, grid) -> int:
        """DFS approach:
        - Time: O(mn)
        - Space: O(mn)
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and not visited[row][col]: self.dfs(row, col, grid, visited)
        return self.perimeter
        
    def dfs(self, row, col, grid, visited):
        if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col] == 0 or visited[row][col] : return
        visited[row][col] = True
        self.perimeter += (4-self.count_neighbors(grid, row, col))
        self.dfs(row-1,col,grid,visited)
        self.dfs(row+1,col,grid,visited)
        self.dfs(row,col-1,grid,visited)
        self.dfs(row,col+1,grid,visited)
        
    def count_neighbors(self, grid, row, col):
        count = 0
        if row-1 >= 0 and grid[row-1][col] == 1: count += 1
        if row+1 < len(grid) and grid[row+1][col] == 1: count += 1
        if col-1 >= 0 and grid[row][col-1] == 1: count += 1
        if col+1 < len(grid[0]) and grid[row][col+1] == 1: count += 1
        return count
