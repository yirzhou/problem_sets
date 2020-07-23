class Solution:
    """#260. Given an array of numbers nums, 
    in which exactly two elements appear only once and all the other elements appear exactly twice. 
    Find the two elements that appear only once
    """
    def singleNumber(self, nums):
        xor = 0
        
        for i in range(len(nums)): xor ^= nums[i]
        
        last_bit_one = xor - (xor & (xor - 1))
        
        group0, group1 = 0, 0
        
        for i in range(len(nums)):
            if last_bit_one & nums[i] == 0: group0 ^= nums[i]
            else: group1 ^= nums[i]
        
        return [group0, group1]
    