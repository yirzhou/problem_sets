import unittest
class Solution:
    """Thought process:
    First, I might want to just sort the array, which takes O(nlg(N)).
    
    But, I realize that it has actually done some work that is not necessary.
    It finds not only the kth largest element, it also finds the (k-1)th, (k-2)th... 
    
    Hence, I can just do partitioning of the array by putting exactly k-1 elements
    on the right of index len(nums)-k where these elements are larger than nums[len(nums)-1].

    I can just keep partitioning until I'm right at len(nums)-k.

    Lesson learned: look for unnecessary work, and optimize from that part. 
    """

    # TODO: implements all sorts of partitioning.
    
    def __init__(self):
        return 

    def findKthLargest(self, nums, k):
        lower, upper = 0, len(nums)-1
        target = len(nums)-k
        while lower <= upper:
            pivot = self.partition(nums, lower, upper)
            if pivot < target:
                lower = pivot+1
            elif pivot > target:
                upper = pivot-1
            else: return nums[pivot]
        
        return -1
        
    def partition(self, nums, lower, upper):
        pivot = nums[upper]
        index = lower

        for i in range(lower, upper):
            if nums[i] <= pivot:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        
        if nums[index] > pivot:
            nums[upper], nums[index] = nums[index], nums[upper]
            return index
        return upper
            

class Test(unittest.TestCase):
    def test_with_negative_numbers(self):
        self.assertEqual(Solution().findKthLargest([3,3,3,3,4,3,3,3,3], 1), 4)

if __name__ == "__main__":
    unittest.main()
            