import unittest

class Solution(object):
    def __init__(self):
        self.paren_count = 0

    def get_closing_paren(self, sentence, opening_paren_index):
        '''It's pretty cool when you can replace a whole data structure with a single integer :)
        '''
        if opening_paren_index < 0 or not len(sentence): raise ValueError('invalid function inputs')
        self.paren_count = 0

        last_closing_paren_index = -1
        for index in range(opening_paren_index, len(sentence)):
            char = sentence[index]
            if char == '(': 
                self.paren_count += 1
            if char == ')': 
                self.paren_count -= 1
                if self.paren_count == 0: 
                    last_closing_paren_index = index
                    return last_closing_paren_index
        
        if self.paren_count: raise ValueError('invalid sentence') 
        return last_closing_paren_index

# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = Solution().get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = Solution().get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            Solution().get_closing_paren('()(()', 2)


unittest.main(verbosity=2)