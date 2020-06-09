class Solution:
    """#845. 
    Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

    - B.length >= 3
    - There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
    (Note that B could be any subarray of A, including the entire array A.)

    Given an array A of integers, return the length of the longest mountain. 
    """
    def longestMountain(self, A):
        """Simple linear-time approach. 
        - Time: O(N)
        - Space: O(1)
        """
        lo, hi = 0, 0
        length = len(A)
        result = 0
        while lo < length:
            hi = lo
            if hi < length - 1 and A[hi]<A[hi+1]:
                while hi < length - 1 and A[hi] < A[hi+1]: hi += 1
                if hi < length - 1 and A[hi] > A[hi+1]: 
                    while hi < length - 1 and A[hi]>A[hi+1]: hi += 1
                    result = max(result, hi - lo + 1)
            lo = max(hi, lo+1)
        return result
                  