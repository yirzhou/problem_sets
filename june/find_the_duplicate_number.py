class Solution:
    """#287. Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
    prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.
    """
    def findDuplicate(self, nums: List[int]) -> int:
        if (len(nums) > 1):

            slow = nums[0]
            fast = nums[nums[0]]
            while (slow != fast):
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            while (fast != slow):
                fast = nums[fast]
                slow = nums[slow]
            
            return slow
        
        return -1
