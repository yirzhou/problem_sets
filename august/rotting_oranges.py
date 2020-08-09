class Solution:
    """#994. In a given grid, each cell can have one of three values:

    - the value 0 representing an empty cell;
    - the value 1 representing a fresh orange;
    - the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
    """
    def orangesRotting(self, grid) -> int:
        fresh = 0
        rotten = []
        row, col = len(grid), len(grid[0])
        
        for i in range(row):
            for j in range(col):
                fresh = fresh+1 if grid[i][j] == 1 else fresh
                if grid[i][j] == 2: rotten.append((i,j,0))
                    
        for i, j, k in rotten:
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= x < row and 0 <= y < col and grid[x][y] == 1:
                    grid[x][y] = 2
                    fresh -= 1
                    rotten.append((x,y,k+1))
        if fresh: return -1
        if not rotten: return 0
        return rotten[-1][-1]
    