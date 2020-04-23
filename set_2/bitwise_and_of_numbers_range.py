from collections import deque
import math

class Solution(object):
    def brute_force(self, m, n):
        if m == 0: return 0

        l = len(bin(m)[2:]) - 1
        i = l
        result = deque()

        while i >= 0:
            if (m // 2**(l-i)) %2 == 0: 
                result.appendleft('0')
            else:
                result.appendleft('1')
                for j in range(m+1, n+1):
                    if (j // 2**(l-i)) %2 == 0:
                        result[0] = '0'
                        break
            i -= 1
        
        return int(''.join(result), 2)

    def range_bitwise_and(self, m, n):
        '''I am essentially shifting both numbers to the right.
        The variable i stores the number of zeros on the rightmost side.
        '''
        i = 0
        while m != n:
            m = m//(2)
            n = n//(2)
            i += 1
        m *= (2**i)
        return m

