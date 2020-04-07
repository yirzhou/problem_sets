class Solution:
    def __init__(self):
        self.result = False

    def isHappy(self, n):
        slow, fast = n, n
        slow = self.__get_sum_of_squares(slow)
        fast == self.__get_sum_of_squares(fast)
        fast == self.__get_sum_of_squares(fast)
        if fast == 1: return True
        print(slow)
        print(fast)
        
        while slow != fast:
            slow = self.__get_sum_of_squares(slow)
            fast == self.__get_sum_of_squares(fast)
            fast == self.__get_sum_of_squares(fast)
            if fast == 1: return True
        return False
    
    def __get_sum_of_squares(self, n):
        result, copy = 0, n
        while copy:
            digit = copy % 10
            result += digit*digit
            copy = (copy - digit)/10
        return result

print(Solution().isHappy(19))
