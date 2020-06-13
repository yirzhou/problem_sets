class Solution:
    """#368. Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
    - Si % Sj = 0 or Sj % Si = 0.

    If there are multiple solutions, return any subset is fine.
    """
    def largestDivisibleSubset(self, nums):
        """DP approach - if a < b and a%b == 0 and b < c and b%c == 0, a%c == 0.
        - Time: O(N^2)
        - Space: O(N)
        """
        if not nums: return []
        nums.sort()
        n = len(nums)
        dp, index = [1] * n, [-1] * n
        max_dp, max_index = 1, 0
        for i in range(n):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    index[i] = j
 
            if max_dp < dp[i]:
                max_dp, max_index = dp[i], i
 
        ans = []
        while max_index != -1:
            ans.append(nums[max_index])
            max_index = index[max_index]
        return ans
