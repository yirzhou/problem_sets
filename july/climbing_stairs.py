class Solution:
    """#70. You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    """
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        memo[0] = 1

        steps = [1,2]

        for level in range(n+1):
            for step in steps:
                if level >= step: memo[level] += memo[level-step]
        
        return memo[n]
