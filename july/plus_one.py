from collections import deque
class Solution:
    """#66.Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

    The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, except the number 0 itself.
    """
    def plusOne(self, digits):
        res = deque(digits)
        res[-1] += 1
        for idx in range(len(res)-2, -1, -1):
            if res[idx+1] >= 10: 
                res[idx+1] -= 10
                res[idx] += 1
        if res[0] >= 10: 
            res[0] = 0
            res.appendleft(1)
        return list(res)