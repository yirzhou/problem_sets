class Solution:
    def threeSum(self, nums):
        results = set()
        results_list = []
        visited = set()
        for index, num in enumerate(nums):
            if num in visited: continue
            visited.add(num)
            partial = self.two_sum(nums, 0-num, index+1)
            for (a,b) in partial:
                result_sorted = sorted([num,a,b])
                result_tuple = tuple(result_sorted)
                if result_tuple not in results: 
                    results_list.append(result_sorted)
                    results.add(result_tuple)
        return results_list
        
        
    def two_sum(self, nums, target, begin):
        if begin > len(nums)-1: return []
        cache = {}
        results = []
        visited = set()
        for i in range(begin, len(nums)):
            if target-nums[i] in cache:
                potential_result = (min(nums[i], target-nums[i]),max(nums[i], target-nums[i]))
                if potential_result not in visited:
                    results.append(potential_result)
                    visited.add(potential_result)
            cache[nums[i]] = i
        return results
    