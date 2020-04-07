class Solution(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0: raise IndexError('cannot use negative index')

        if n in [0,1]: return n

        if n in self.memo: return self.memo[n]

        result = self.fib(n-1) + self.fib(n-2)
        self.memo[n] = result
        return result

    def fib_iterative(self, n):

        # Compute the nth Fibonacci number

        if n < 0: raise ValueError('invalid input')
        if n == 0: return 0
        if n == 1: return 1
        
        before_prev, prev = 0, 1
        fbnc = 0
        for _ in range(2, n+1):
            fbnc = prev + before_prev
            before_prev, prev = prev, fbnc
        
        return fbnc

        