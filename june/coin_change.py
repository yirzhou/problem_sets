class Solution:
    """#518. You are given coins of different denominations and a total amount of money. 
    Write a function to compute the number of combinations that make up that amount. 
    You may assume that you have infinite number of each kind of coin.
    """
    def change(self, amount, coins):
        """Bottom-up approach; k = number of types of coin, N = amount.
        - Time: O(kN)
        - Space: O(N)
        """
        memo = [0]*(amount+1)
        memo[0] = 1
        for coin in coins:
            for i in range(1, amount+1):
                if coin <= i: memo[i] += memo[i-coin]
        return memo[amount]
    