class Solution:
    """#123. Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.

    Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
    """
    def maxProfit(self, prices) -> int:
        if len(prices) == 0: return 0
        
        s1, s2, s3, s4 = -prices[0], float("-inf"), float("-inf"), float("-inf")
        
        for i in range(1, len(prices)):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1+prices[i])
            s3 = max(s3, s2-prices[i])
            s4 = max(s4, s3+prices[i])
        
        return max(0, s4)
