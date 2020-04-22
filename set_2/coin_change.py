class Solution:
    '''You are given coins of different denominations and a total amount of money amount. 
    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    '''
    def coin_change(self, coins: List[int], amount: int) -> int:
        '''Yet again another classic example of the knapsack problem. 
        The idea is to update the lowest number of coins each time when adding a new coin.
        - Space: O(k) where k is the amount.
        - Time: O(N*k) where N is the number of coins.
        '''
        mem = [-1]*(amount+1)
        mem[0] = 0
        
        for coin in coins:
            for val in range(coin, amount+1):
                if mem[val-coin] != -1: mem[val] = min(mem[val], 1+mem[val-coin]) if mem[val] != -1 else 1+mem[val-coin]

        return mem[amount]
        