class Solution:
    """#154. Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

    (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

    Find the minimum element.

    The array may contain duplicates.
    """
    def findMin(self, nums) -> int:
        begin, end = -1, len(nums)
        min_index = 0
        
        while begin+1 < end:
            mid = begin + (end-begin) // 2
            
            if nums[mid] > nums[min_index]:
                begin = mid
            elif nums[mid] < nums[min_index]:
                min_index = mid
                end = mid 
            else:
                break
        
        for ind in range(1, len(nums), 1):
            diff = nums[ind] - nums[ind - 1]
            if diff < 0: return nums[ind]
        
        return nums[min_index]
