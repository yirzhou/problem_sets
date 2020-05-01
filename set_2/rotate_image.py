class Solution:
    '''You are given an n x n 2D matrix representing an image.
    Rotate the image by 90 degrees (clockwise) in place!
    '''

    def rotate(self, matrix) -> None:
        '''This algorithm uses some mathematical tricks.
        The main idea is to swap four values each time from outer circle
        down to inner circle. Say we have an n*n matrix, thus we are 
        swapping values on the n*n square, (n-2)*(n-2) square, and so on.
        '''
        dimension = len(matrix)
        upper = dimension**2-1
        
        begin, end = 0, dimension-1
        iteration = 0
        
        while begin < end:
            diff = end-begin
            d = diff+1
            for i in range(diff):
                lu = i+(iteration)*dimension+iteration
                ru = lu+(diff-i)+i*dimension
                rb = upper - i - (dimension+1)*iteration
                lb = rb - (diff-i)-i*dimension
                matrix[lu//dimension][lu%dimension], \
                matrix[ru//dimension][ru%dimension], \
                matrix[rb//dimension][rb%dimension], \
                matrix[lb//dimension][lb%dimension] = \
                matrix[lb//dimension][lb%dimension], \
                matrix[lu//dimension][lu%dimension], \
                matrix[ru//dimension][ru%dimension], \
                matrix[rb//dimension][rb%dimension]
                
            begin += 1
            end -= 1
            iteration += 1

sol = Solution()

# matrix = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]

# print(matrix)
# sol.rotate(matrix)
# print(matrix)

# matrix2 = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# print(matrix2)
# sol.rotate(matrix2)
# print(matrix2)

matrix3 = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36]
]

print(matrix3)
sol.rotate(matrix3)
print(matrix3)