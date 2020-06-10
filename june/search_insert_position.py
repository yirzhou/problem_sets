class Solution:
    """#35. Given a sorted array and a target value, return the index if the target is found. 
    If not, return the index where it would be if it were inserted in order.
    """
    def searchInsert(self, nums, target):
        lo, hi = 0, len(nums)-1
        
        while lo < hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target: return mid
            else:
                if nums[mid] > target: hi = mid-1
                else: lo = mid+1
        
        if nums[lo] < target: return lo+1
        elif nums[lo] > target: 
            if lo == 0: return 0
            else:
                if nums[lo-1] < target < nums[lo]: return lo
                else: return lo-1
        return lo
