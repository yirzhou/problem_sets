class Solution:
    """LC #1262. Given an array nums of integers, find the maximum possible sum of elements of the array such that it is divisible by three."""
    def maxSumDivThree(self, nums: List[int]) -> int:
        """DP approach:
        - Time: O(N)
        - Space: O(1)
        """
        memo = [0,0,0]
        
        for num in nums:
            pre_memo = memo.copy()
            for i in range(3):
                cur_sum = num+pre_memo[i]
                remainder = cur_sum%3
                memo[remainder]=max(memo[remainder], cur_sum)
        return memo[0]
                