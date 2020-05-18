class Solution:
    """#204. Count the number of prime numbers less than a non-negative number, n."""
    def count_primes(self, n: int) -> int:
        """Sieve of Eratosthenes.
        - Time: O(n*sqrt(n))
        """
        marked = [False]*n
        primes = 0
        for i in range(2, n):
            if not marked[i]: 
                primes += 1
                start = i
                multiple = start*i
                while multiple < n:
                    marked[multiple] = True
                    start += 1
                    multiple = start*i
        return primes
        