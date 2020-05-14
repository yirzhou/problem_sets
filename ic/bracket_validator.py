import unittest
import unittest

class Solution(object):
    def __init__(self):
        self.index = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

    def is_valid(self, code):
        stack = []

        for char in code:
            if char in self.index:
                if len(stack) and stack[-1] == self.index[char]: stack.pop()
                else: return False
            else:
                stack.append(char)
        
        return len(stack) == 0

# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = Solution().is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = Solution().is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = Solution().is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = Solution().is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = Solution().is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = Solution().is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = Solution().is_valid('')
        self.assertTrue(result)

unittest.main(verbosity=2)
