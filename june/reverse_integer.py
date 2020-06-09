import math
class Solution:
    """#7. Given a 32-bit signed integer, reverse digits of an integer."""
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        
        negative = False
        if x < 0: 
            x *= -1
            negative = True
        multiplier = 10**math.floor(math.log10(x))
        
        digits = []
        
        while x != 0:
            digit = int(x//multiplier)
            digits.append(digit)
            x -= digit*multiplier
            multiplier /= 10

        multi = 1
        result = 0
        for i in range(0, len(digits)):
            result += digits[i]*multi
            multi *= 10
        
        if negative: result *= -1
        return result if -(2**31) <= result <= 2**31-1 else 0
        