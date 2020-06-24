class Solution:
    """#96. Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?"""
    def numTrees(self, n: int) -> int:
        count = [0]*(n+1)
        count[0], count[1] = 1, 1
        
        for i in range(2, n+1):
            for j in range(i):
                count[i] += count[j]*count[i-j-1]
        return count[n]
    