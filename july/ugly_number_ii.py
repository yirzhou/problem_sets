import math 
class Solution:
    """#264. Write a program to find the n-th ugly number.

    Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
    """
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0: return 0
        uglies = [1]
        
        two, three, five = 0, 0, 0
        while len(uglies) < n:
            by_two, by_three, by_five = uglies[two]*2, uglies[three]*3, uglies[five]*5
            minimum = min(by_two, by_three, by_five)
            uglies.append(minimum)
            
            if minimum == by_two: two += 1
            if minimum == by_three: three += 1
            if minimum == by_five: five += 1
        return uglies[-1]
