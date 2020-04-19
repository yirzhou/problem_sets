class Solution(object):
    def __init__(self):
        return

    def search_sorted(self, nums, target):
        '''Find the rotation point, then do search on one half. This is probably not the optimal solution.
        1. find the pivot index
        2. do search on one half of the array
        3. worst case: do search on the entire array
        
        This gives constant space complexity, and O(log(N)) time complexity.
        '''
        if len(nums) == 0: return -1
        pivot = self.__find_pivot(nums)

        # first case: pivot is the first
        if pivot == 0:
            if target > nums[len(nums)-1] or target < nums[0]: return -1
            return self.__search(nums, -1, len(nums), target)
        # second case: pivot in the middle
        else:
            if target <= nums[len(nums)-1]: return self.__search(nums, pivot-1, len(nums), target)
            else: return self.__search(nums, -1, pivot, target)

        return -1

    def __find_pivot(self, nums):

        begin, end = 0, len(nums)-1

        while begin + 1 < end:
            mid = begin + (end-begin)//2
            if nums[mid] > nums[0]: begin = mid
            else: end = mid
        
        if nums[begin] > nums[end]:
            if nums[end] > nums[0]: return 0
            else: return end
        else:
            if nums[begin] > nums[0]: return 0
            else: return begin

    def __search(self, nums, begin, end, target):

        if begin == end and nums[begin] == target: return begin

        while begin + 1 < end:
            mid = begin + (end-begin)//2
            if nums[mid] > target: end = mid
            elif nums[mid] < target: begin = mid
            else: return mid
        return -1

    def search(self, nums, target):
        if len(nums) == 0: return -1
        if len(nums) == 1: return -1 if nums[0] != target else 0
        if len(nums) == 2: 
            if nums[0] == target: return 0
            if nums[1] == target: return 1
            return -1

        begin, end = 0, len(nums)-1

        while begin <= end:
            mid = begin + (end-begin)//2
            if nums[mid] == target: return mid
            elif nums[mid] >= nums[begin]:
                if nums[begin] <= target < nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    begin = mid + 1
                else:
                    end = mid - 1
        return -1

print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([1,2,3,4,7], 7))
print(Solution().search([5,1,3], 5))
