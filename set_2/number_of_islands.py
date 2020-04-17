import unittest

class Solution:
    """Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
    You may assume all four edges of the grid are all surrounded by water.
    """
    def __init__(self): 
        self.visited = set()
        self.number_of_islands = 0
        self.x_limit, self.y_limit = 0, 0
        self.stack = []

    def __clear(self):
        self.visited.clear()
        self.stack.clear()
        self.number_of_islands = 0

    def num_islands(self, grid):
        """Solving the problem in an iterative fashion. 
        Given R and C as the number of rows and columns in the grid, and N as the number of '1's:
        - Time complexity: O(N) since it avoids visiting the '0's.
        - Space complexity: O(N) since only '1's are pushed onto the stack and into the set. 
        """
        
        if not len(grid): return 0

        self.__clear()
        self.y_limit, self.x_limit = len(grid), len(grid[0])

        for y, row in enumerate(grid):
            for x, item in enumerate(row):
                if item == '1' and (y, x) not in self.visited:
                    self.stack.append((y,x))
                while len(self.stack):
                    y_pos, x_pos = self.stack.pop()
                    if (y_pos, x_pos) not in self.visited:
                        self.visited.add((y_pos, x_pos))
                        self.number_of_islands += 1
                    self.__explore(grid, y_pos, x_pos)

        return self.number_of_islands

    def __explore(self, grid, y, x):

        if y-1 > -1 and grid[y-1][x] == '1' and (y-1, x) not in self.visited:
            self.stack.append((y-1, x))
            self.visited.add((y-1, x))
        if y+1 < self.y_limit and grid[y+1][x] == '1' and (y+1, x) not in self.visited:
            self.stack.append((y+1, x))
            self.visited.add((y+1, x))
        if x-1 > -1 and grid[y][x-1] == '1' and (y, x-1) not in self.visited:
            self.stack.append((y, x-1))
            self.visited.add((y, x-1))
        if x+1 < self.x_limit and grid[y][x+1] == '1' and (y, x+1) not in self.visited:
            self.stack.append((y, x+1))
            self.visited.add((y, x+1))
        

class Test(unittest.TestCase):
    
    def test_one_island(self):
        self.assertEqual(1, 
            Solution().num_islands([
            ['1','1','1','1','0'],
            ['1','1','0','1','0'],
            ['1','1','0','0','0'],
            ['0','0','0','0','0']
        ]))
    
    def test_three_islands(self):
        self.assertEqual(3, 
            Solution().num_islands([
            ['1','1','0','0','0'],
            ['1','1','0','0','0'],
            ['0','0','1','0','0'],
            ['0','0','0','1','1']
        ]))
    
    def test_random(self):
        self.assertEqual(1, Solution().num_islands([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))

unittest.main(verbosity=2)
