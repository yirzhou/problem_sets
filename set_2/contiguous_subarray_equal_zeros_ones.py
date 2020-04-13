import unittest

class Solution(object):
    '''Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
    '''
    def __init__(self): return

    def find_max_length(self, nums):
        '''A bottom up, dynamic programming approach. 
        The main idea is to check the current difference between zero count and one count.
        Then, find the smallest index at which the zero count and one count have the same difference.
        This means that over these iterations, we have seen the same growth for zeros and ones.
        - O(N) time
        - O(N) space in worst case
        '''
        if len(nums) < 2: return 0

        cache_more_zeros, cache_more_ones = {}, {}
        zeros, ones, max_length = 0, 0, 0

        for index, num in enumerate(nums):
            if num == 0: zeros += 1
            if num == 1: ones += 1

            if zeros == ones: max_length = max(max_length, zeros*2)
            else:
                if zeros > ones:
                    diff = zeros - ones
                    if diff not in cache_more_zeros: cache_more_zeros[diff] = index
                    else: max_length = max(max_length, index-cache_more_zeros[diff])
                else:
                    diff = ones - zeros
                    if diff not in cache_more_ones: cache_more_ones[diff] = index
                    else: max_length = max(max_length, index-cache_more_ones[diff])
        return max_length

    def brute_force(self, nums):
        zeros, ones, max_len = 0, 0, 0
        for i in range(len(nums)):
            zeros, ones = 0, 0
            if nums[i] == 0: zeros += 1
            if nums[i] == 1: ones += 1
            for j in range(i + 1, len(nums)):
                if nums[j] == 0: zeros += 1
                if nums[j] == 1: ones += 1
                if zeros == ones: 
                    max_len = max(max_len, 2*zeros)
        return max_len

class Test(unittest.TestCase):

    def test_zero_length(self):
        self.assertEqual(0, Solution().find_max_length([0]))
    
    def test_length_of_one(self):
        self.assertEqual(0, Solution().find_max_length([]))

    def test_four_consecutive_zeros(self):
        self.assertEqual(4, Solution().find_max_length([0,0,0,0,1,1,0]))

    def test_mixed(self):
        self.assertEqual(6, Solution().find_max_length([1,1,0,1,0,0,1]))

    def test_all_zeros(self):
        self.assertEqual(0, Solution().find_max_length([0,0,0,0,0,0,0,0]))
    
    def test_long(self):
        nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
        self.assertEqual(68, Solution().find_max_length(nums))

    def test_brute_force(self):
        nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
        self.assertEqual(68, Solution().brute_force(nums))

unittest.main(verbosity=2)
