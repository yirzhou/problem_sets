from collections import deque
from itertools import islice
class Solution:
    """#402:
    Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
    """
    def remove_k_digits(self, num: str, k: int) -> str:
        """Idea is to remove the most significant bits, from right to left as new digits come in.
        - Time: O(N*k)
        - Space: O(N)
        """
        l = len(num)
        if k == l: return '0'
        d = l-k
        min_list = deque([])
        
        for digit in num:
            while k > 0 and len(min_list) and int(min_list[-1])>int(digit): 
                min_list.pop()
                k -= 1
            min_list.append(digit)
        
        min_list = deque(islice(min_list, 0, d))
        while len(min_list) and min_list[0] == '0': min_list.popleft()
        result = ''.join(min_list)
        return result if len(result) else '0'
            