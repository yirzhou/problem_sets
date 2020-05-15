class Solution:
    """Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C."""
    def max_subarray_sum_circular(self, A) -> int:
        """An extension of Kadane's algorithm.
        The maximum sum and the minimum sum will be tracked (of subarrays).
        The total sum - minimum sum could be the maximum sum.
        However, if the max sum is negative, we directly return it because
        total - min will be zero, which is not what we want. 
        """
        max_sum, local_hi = float('-inf'), float('-inf')
        min_sum, local_min = float('inf'), float('inf')
        total = 0
        
        for num in A:
            local_hi = max(num, local_hi+num)
            max_sum = max(max_sum, local_hi)
            
            local_min = min(num, local_min+num)
            min_sum = min(min_sum, local_min)
            total += num
            
        return max_sum if max_sum < 0 else max(max_sum, total-min_sum)
        