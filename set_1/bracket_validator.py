class Solution(object):
    def __init__(self): 
        self.stack = []
        self.closers = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

    def __reset(self): self.stack.clear()

    def is_valid(self, code):
        '''
        Two common uses for stacks are:

        1. parsing (like in this problem)
        2. tree or graph traversal (like depth-first traversal)
        '''
        self.__reset()
        
        for char in code:
            if char in self.closers: self.stack.append(char)
            else:
                if len(self.stack) == 0: return False
                if self.closers[char] != self.stack[len(self.stack)-1]: return False
                self.stack.pop()
        
        return True if len(self.stack) == 0 else False
