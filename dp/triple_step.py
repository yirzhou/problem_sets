class Solution:
    """Question 8.1.
    """
    def triple_steps(self, n):
        memo = [0]*(n+1)
        memo[0] = 1
        steps = [1,2,3]
        for level in range(n+1):
            for step in steps:
                if level >= step: memo[level] += memo[level-step]
        
        return memo[n]

print(Solution().triple_steps(2))