class Solution:
    """LC #377: Given an integer array with all positive numbers and no duplicates, 
    find the number of possible combinations that add up to a positive integer target."""
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Dynamic programming approach.
        The idea is to gradually expand our target and build up the number of ways
        to get to the target from previous built-up smaller targets.

        - Space: O(n) where n is the target
        - Time: O(k*n) where k is the number of items in the list. 
        """
        memo = [0]*(target+1)
        memo[0] = 1
        
        for t in range(1, target+1):
            for num in nums:
                if num <= t: memo[t] += memo[t-num]
                    
        return memo[target]
