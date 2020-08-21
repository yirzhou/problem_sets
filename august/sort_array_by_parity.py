class Solution:
    """#905. Given an array A of non-negative integers, 
    return an array consisting of all the even elements of A, 
    followed by all the odd elements of A.

    You may return any answer array that satisfies this condition.
    """
    def sortArrayByParity(self, A):
        return [i for i in A if i%2==0] + [i for i in A if i%2!=0]
