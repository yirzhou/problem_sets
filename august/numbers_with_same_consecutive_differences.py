class Solution:
    """#967. Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

    Note that every number in the answer must not have leading zeros except for the number 0 itself. 
    For example, 01 has one leading zero and is invalid, but 0 is valid.

    You may return the answer in any order.
    """
    def numsSameConsecDiff(self, N: int, K: int):
        if N == 1: return [i for i in range(10)]
        a = [i for i in range(1,10)]
        
        for i in range(1, N):
            b = []
            M = len(a)
            for j in range(M):
                x = a[j]
                d = x%10
                if d+K <= 9: b.append(x*10+d+K)
                if d-K >= 0 and d+K != d-K: b.append(x*10+d-K)
            a=b
        return a
