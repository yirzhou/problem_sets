# from collections import defaultdict

class Solution:
    def findMaxLength(self, nums) -> int:
        """#525. Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
        - Time: O(N)
        - Space: O(N) in worst case
        """
        memo = [None] * (2*len(nums)+1)
        memo[0] = 0
        zeros, ones = 0, 0
        max_len = 0
        
        for index, val in enumerate(nums):
            if val == 0: zeros += 1
            else: ones += 1
            diff = zeros-ones

            if memo[diff] != None:
                max_len = max(max_len, index-memo[diff]+1)
            else:
                memo[diff] = index+1
           
        return max_len
