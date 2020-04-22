import unittest
import heapq

class Solution(object):
    def __init__(self):
        self.min_sum = float('inf')
        self.m, self.n = 0, 0

    def min_path_sum(self, grid):
        self.m = len(grid)
        if self.m == 1: return sum(grid[0])
        if self.m == 0: return 0

        self.n = len(grid[0])

        self.__dfs(grid, 0, 0, 0)
        return self.min_sum

    def __dfs(self, grid, m, n, current_sum):   
        """The brute force solution:
        - Time complexity: O(2^m*n)
        - Space complexity: O(m*n)
        """ 
        current_sum += grid[m][n]
        if m == self.m-1 and n == self.n-1:
            self.min_sum = min(self.min_sum, current_sum)
    
        if m+1 < self.m: 
            current_sum = self.__dfs(grid, m+1, n, current_sum)
        if n+1 < self.n:
            current_sum = self.__dfs(grid, m, n+1, current_sum)
        current_sum -= grid[m][n]
        return current_sum
    
class ShortestPath(object):
    def __init__(self):
        self.from_point = {}
        # (m, n)
        self.visited = set()
        # {cost, (m, n)}
        self.heap = []
        self.m, self.n = 0, 0
    
    def __clear(self):
        self.from_point.clear()
        self.visited.clear()
        self.heap.clear()

    def min_path_sum(self, grid):
        '''OSPF algorithm.
        '''
        self.__clear()
        self.m = len(grid)
        if self.m == 1: return sum(grid[0])
        if self.m == 0: return 0
        self.n = len(grid[0])

        heapq.heappush(self.heap, (grid[0][0], 0, 0))
        self.from_point[(0,0)] = grid[0][0]
        while len(self.heap):
            cost_so_far, m, n = heapq.heappop(self.heap)

            if (m, n) in self.visited: continue
            self.visited.add((m, n))

            # cost = cost_so_far + grid[m][n]
            if (m, n) not in self.from_point or cost_so_far < self.from_point[(m, n)]: self.from_point[(m, n)] = cost_so_far

            if (m, n) == (self.m-1, self.n-1): return self.from_point[(m,n)]
            self.get_neighbor(self.from_point[(m, n)], grid, m, n)

        return self.from_point[(m,n)]
        

    def get_neighbor(self, cost_so_far, grid, m, n):
        if m+1 < self.m: heapq.heappush(self.heap, (cost_so_far+grid[m+1][n], m+1, n))
        if n+1 < self.n: heapq.heappush(self.heap, (cost_so_far+grid[m][n+1], m, n+1))

class GreedySolution(object):
    def __init__(self):
        return

    def min_path_sum(self, grid):
        '''A bottom up approach.
        '''
        m = len(grid)
        n = len(grid[0])
        pre = [grid[0][0]] * m
        cur = [0] * m
        
        for i in range(1, m):
            pre[i] = pre[i - 1] + grid[i][0]
            
        for i in range(1, n):
            cur[0] = pre[0] + grid[0][i]
            for j in range(1, m):
                cur[j] = min(cur[j - 1], pre[j]) + grid[j][i]
            pre, cur = cur, pre
        
        return pre[m - 1]

class Test(unittest.TestCase):
    def test_large_grid(self):
        self.assertEqual(47, ShortestPath().min_path_sum([[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]))

    def test_small_grid(self):
        self.assertEqual(7, ShortestPath().min_path_sum([[1,3,1],[1,5,1],[4,2,1]]))
    
    def test_medium(self):
        self.assertEqual(27, ShortestPath().min_path_sum([[7,0,8,8,0,3,5,8,5,4],[4,1,2,9,9,6,0,8,6,9],[9,7,1,1,0,1,2,4,1,7]]))

unittest.main(verbosity=2)
