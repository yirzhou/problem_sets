class Solution:
    """#1277. Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
    - Similar to #211: Maximal Square.
    """
    def count_squares(self, matrix):
        """DP Approach:
        - Time: O(m*n)
        - Space: O(1)
        """
        square_count = 0
        m, n = len(matrix), len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col] != 0:
                    if row > 0 and col > 0:
                        matrix[row][col] = min(matrix[row][col-1], matrix[row-1][col], matrix[row-1][col-1])+1
                square_count += matrix[row][col]
        return square_count
    
    def countSquares(self, matrix) -> int:
        """Optimized brute-force solution:
        - Time: O(min(m,n)*m*n)
        - Space: O(1)
        """
        m, n = len(matrix), len(matrix[0])
        square_count = 0
        max_dimension = min(m, n)
        
        for d in range(max_dimension):
            for row in range(m-d):
                for col in range(n-d):
                    if self.is_square(row, col, d+1, matrix): 
                        square_count += 1
                        matrix[row][col] = d+1
        return square_count
        
    def is_square(self, row, col, dimension, matrix):
        if dimension == 1: return matrix[row][col] == 1
        else:
            sub_dimension = dimension-1
            return matrix[row][col] == sub_dimension and \
                   matrix[row+1][col] == sub_dimension and \
                   matrix[row][col+1] == sub_dimension and \
                   matrix[row+1][col+1] == sub_dimension
