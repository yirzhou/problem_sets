import unittest

class Solution(object):

    def __init__(self): return

    def valid_parenthesis_string(self, string):
        if len(string) == 0: return True

        left_stack, star_stack, right_stack = [], [], []

        for index, char in enumerate(string):
            if char == '(': 
                left_stack.append((index, '('))
            if char == ')': 
                if len(left_stack) == 0 and len(star_stack) == 0: return False
                if len(left_stack): left_stack.pop()
                elif len(left_stack) == 0 and len(star_stack): right_stack.append((index, ')'))
            if char == '*':
                star_stack.append((index, '*'))
        
        # post processing
        if len(left_stack):
            while len(left_stack) and len(star_stack):
                left_index = left_stack[len(left_stack)-1][0]
                star_index, _ = star_stack.pop()
                if left_index < star_index: left_stack.pop()
        if len(right_stack):
            while len(right_stack) and len(star_stack):
                right_index = right_stack[len(right_stack)-1][0]
                star_index, _ = star_stack.pop()
                if star_index < right_index: right_stack.pop()
        return len(left_stack) == 0 and len(right_stack) == 0
    
class Test(unittest.TestCase):

    def test_all_stars(self):
        self.assertEqual(True, Solution().valid_parenthesis_string('*********'))

    def test_random_mix(self):
        self.assertEqual(True, Solution().valid_parenthesis_string('(*)*(()*'))

    def test_random(self):
        self.assertEqual(True, Solution().valid_parenthesis_string('*)(*'))

    def test_invalid_left(self):
        self.assertEqual(False, Solution().valid_parenthesis_string('(*('))
    
    def test_invalid_right(self):
        self.assertEqual(False, Solution().valid_parenthesis_string(')*)*'))

    def test_valid_long(self):
        self.assertEqual(False, Solution().valid_parenthesis_string("()(*(*()()(*)(()())((*))()(()(*((*)))))*)()(()))(("))

unittest.main(verbosity=2)
