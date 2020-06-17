from collections import deque
class Solution:
    """#130.Given a 2D board containing 'X' and 'O' (the letter O), 
    capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region."""
    def solve(self, board):
        """BFS Approach.
        - Time: O(mn)
        - Space: O(mn)
        """
        m = len(board)
        if m == 0: return 
        n = len(board[0])
        do_not_touch = [[False for _ in range(n)] for _ in range(m)]
        in_queue = [[False for _ in range(n)] for _ in range(m)]
        queue = deque()
        
        self.preprocess(board,queue,m,n,in_queue)
        while len(queue):
            (row,col) = queue.popleft()
            do_not_touch[row][col] = True
            self.push_neighbors(board,row,col,m,n,queue,in_queue)
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and not do_not_touch[row][col]:
                    board[row][col] = 'X'
    
    
    def push_neighbors(self,board,row,col,m,n,queue,in_queue):
        if self.is_valid(row-1,col,board,m,n) and not in_queue[row-1][col]:
            queue.append((row-1,col))
            in_queue[row-1][col] = True
        if self.is_valid(row+1,col,board,m,n) and not in_queue[row+1][col]:
            queue.append((row+1,col))
            in_queue[row+1][col] = True
        if self.is_valid(row,col-1,board,m,n) and not in_queue[row][col-1]:
            queue.append((row,col-1))
            in_queue[row][col-1] = True
        if self.is_valid(row,col+1,board,m,n) and not in_queue[row][col+1]:
            queue.append((row,col+1))
            in_queue[row][col+1] = True
        
        
    def preprocess(self, board, queue, m, n,in_queue):
        for row in range(m):
            if board[row][0] == 'O' and not in_queue[row][0]: 
                queue.append((row, 0))
                in_queue[row][0] = True
            if board[row][n-1] == 'O' and not in_queue[row][n-1]: 
                queue.append((row, n-1))
                in_queue[row][n-1] = True
        for col in range(n):
            if board[0][col] == 'O' and not in_queue[0][col]: 
                queue.append((0, col))
                in_queue[0][col] = True
            if board[m-1][col] == 'O' and not in_queue[m-1][col]: 
                queue.append((m-1, col))
                in_queue[m-1][col] = True
        
    def is_valid(self,row,col,board,m,n):
        return 0 <= row < m and 0 <= col < n and board[row][col] == 'O'
    