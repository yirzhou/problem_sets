from collections import deque
from math import factorial
class Solution:
    """#60. The set [1,2,3,...,n] contains a total of n! unique permutations.
    By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
    - "123"
    - "132"
    - "213"
    - "231"
    - "312"
    - "321"

    Given n and k, return the kth permutation sequence.
    """
    def getPermutation(self, n: int, k: int) -> str:
        nums = [num for num in range(1,n+1)]
        if k == 1: return ''.join([str(num) for num in nums])
        pre_list = []
        fact = factorial(n-1)
        quotient = k//fact
        remainder = k%fact
        i = 1
        while quotient != 0 and quotient < len(nums):
            if remainder == 0:
                pre_list.append(str(nums[quotient-1]))
                nums = nums[0:quotient-1]+nums[quotient:]
            else:
                pre_list.append(str(nums[quotient]))
                nums = nums[0:quotient]+nums[quotient+1:]
            i -= 1
            fact = factorial(n-i)
            quotient = remainder//fact
            remainder = remainder%fact
        
        for i in range(len(nums)): nums[i] = str(nums[i])
        sub = self.permute(nums,remainder)
        pre_list.append(sub)
        return ''.join(pre_list)

    def permute(self, l, k):
        dq = deque(l)
        perms = self.get_perms(dq)
        for i in range(len(perms)):
            perms[i] = int(perms[i])
        perms.sort()
        return str(perms[k-1])

    def get_perms(self, dq):
        if len(dq) == 1: return [str(dq[0])]
        if len(dq) == 2: return [''.join([str(dq[0]), str(dq[1])]), ''.join([str(dq[1]), str(dq[0])])]

        perms = []
        for _ in range(len(dq)):
            current = dq.popleft()
            rest = self.get_perms(dq)
            for substr in rest: perms.append(current + substr)
            dq.append(current)
        return perms
