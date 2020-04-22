class Solution:
    def subarray_sum(self, nums, k):
        '''Brute force solution using cache. 
        - Time complexity: O(N^2), which is quadratic.
        '''
        cache = {}
        total_sum, count = 0, 0

        for i, num in enumerate(nums):
            total_sum += num
            if total_sum == k: count += 1
            cache[(0,i)] = total_sum
            for j in range(i):
                cache[(j+1,i)] = cache[(0,i)] - cache[(0,j)]
                if cache[(j+1,i)] == k: count += 1
        return count

    def subarray_sum_optimized(self, nums, k):
        '''Optimized approach using hash map.
        - Time: O(N)
        - Space: O(N)
        '''
        cache = {}
        total, count = 0, 0

        cache[0] = 1

        for num in nums:
            total += num
            if total not in cache: cache[total] = 0
            cache[total] += 1
            
            diff = total - k
            if diff in cache: count += cache[diff]
        
        return count
        