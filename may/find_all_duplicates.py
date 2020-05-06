class Solution:
    """Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), 
    some elements appear twice and others appear once.
    Find all the elements that appear twice in this array."""
    def find_duplicates(self, nums: List[int]) -> List[int]:
        """A linear-time algorithm"""
        duplicates = []
        
        for num in nums:
            if num > 0: 
                if nums[num-1] < 0: duplicates.append(num)
                else: nums[num-1] *= -1
            else:
                if nums[(-num)-1] < 0: duplicates.append(-num)
                else: nums[(-num)-1] *= -1
        
        return duplicates
                