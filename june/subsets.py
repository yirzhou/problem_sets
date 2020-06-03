class Solution:
    """#78. Given a set of distinct integers, nums, return all possible subsets (the power set).
    Note: The solution set must not contain duplicate subsets.
    """
    def subsets(self, nums):
        subsets = [[]]
        
        for num in nums:
            sets = []
            for sub in subsets:
                copy_sub = sub.copy()
                copy_sub.append(num)
                sets.append(copy_sub)
            subsets.extend(sets)
        return subsets
        