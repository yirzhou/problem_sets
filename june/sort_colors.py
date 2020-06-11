class Solution:
    """#75. Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, 
    with the colors in the order red, white and blue.
    Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
    """
    def sortColors(self, nums):
        """The Dutch Partitioning Problem in linear-time, constant space."""
        red,white,blue = 0,0,len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red],nums[white] = nums[white],nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        