class Solution:
    """#119. Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

    Note that the row index starts from 0.
    """
    def getRow(self, rowIndex: int):
        row = [0]*(rowIndex+1)
        row[0] = 1
        
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                row[j] += row[j-1]
        return row
