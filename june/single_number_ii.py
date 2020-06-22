class Solution:
    """#137. Given a non-empty array of integers, 
    every element appears three times except for one, 
    which appears exactly once. 
    Find that single one.
    """
    def singleNumber(self, nums) -> int:
        """This is a very trickey bitwise solution that takes constant space
        and linear time
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones^num)& ~twos
            twos = (twos^num)& ~ones
        return ones
    