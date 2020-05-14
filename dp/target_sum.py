from collections import defaultdict;
class Solution:
    """LC #494
    You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
    Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
    Find out how many ways to assign symbols to make sum of integers equal to target S."""
    def __init__(self):
        self.count = 0

    def find_target_sum_ways(self, nums, S) -> int:
        """Dynamic programming approach:
        - Time: O(N^2)
        - Space: O(N^2)
        """
        length = len(nums)
        memo = []
        for i in range(length+1): memo.append(defaultdict())
        memo[0][0] = 1

        for i in range(1, length+1):
            for key in memo[i-1]:
                if key+nums[i-1] not in memo[i]: memo[i][key+nums[i-1]] = 0
                memo[i][key+nums[i-1]] += memo[i-1][key]
                if key-nums[i-1] not in memo[i]: memo[i][key-nums[i-1]] = 0
                memo[i][key-nums[i-1]] += memo[i-1][key]
        
        return memo[length].get(S, 0)

    def __find_target(self, begin, nums, current_sum, target):
        """Brute force solution that takes O(2^n) time"""

        if begin == len(nums)-1:
            if current_sum + nums[begin] == target: self.count += 1
            if current_sum - nums[begin] == target: self.count += 1
        else:
            self.__find_target(begin+1, nums, current_sum+nums[begin], target)
            self.__find_target(begin+1, nums, current_sum-nums[begin], target)
        return

        

sol = Solution()
print(sol.find_target_sum_ways([1,1,1,1,1], 3))
print(sol.find_target_sum_ways([1,2], 3))