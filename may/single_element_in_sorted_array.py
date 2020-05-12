class Solution:
    """#540
    You are given a sorted array consisting of only integers where every element appears exactly twice, 
    except for one element which appears exactly once. Find this single element that appears only once."""
    def single_non_duplicate(self, nums) -> int:
        """Approach using binary search:
        - Time: O(lg(N))
        - Space: O(1)
        """
        length = len(nums)
        begin, end = 0, length-1
        
        while begin < end:
            mid = begin + (end-begin) // 2
            
            if mid > 0 and mid < length-1:
                if nums[mid] == nums[mid-1]:
                    if (mid-begin+1)%2: end = mid
                    else: begin = mid+1
                elif nums[mid] == nums[mid+1]:
                    if (end-mid+1)%2: begin = mid
                    else: end = mid-1
                else: return nums[mid]
            else:
                return nums[mid]
        
        return nums[begin]
    