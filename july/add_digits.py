class Solution:
    """#258. Given a non-negative integer num, repeatedly add all its digits until the result has only one digit."""
    def addDigits(self, num: int) -> int:
        res = 0
        while num > 0:
            res += num % 10
            num = num // 10
            
            if num == 0 and res > 9:
                num = res
                res = 0
        return res
    
    def digital_root(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
