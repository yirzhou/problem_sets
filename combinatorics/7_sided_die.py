import random


def rand5():
    return random.randint(1, 5)

def rand7_rudimentary():
    '''This is a truly fascinating idea.
    While there are some zeros, the numbers of 1's through 7's
    in the matrix are even, so they have the same probability
    to be generated regardless of the zeros.
    '''

    vals = [
        [1,2,3,4,5],
        [6,7,1,2,3],
        [4,5,6,7,1],
        [2,3,4,5,6],
        [7,0,0,0,0]
    ]

    i, j = rand5(), rand5()
    result = vals[i-1][j-1]

    while result == 0:
        i, j = rand5(), rand5()
        result = vals[i-1][j-1]
    return result

def rand7():
    '''This is an optimized version, but still has a worst-case O(infinity) runtime.
    Actually, the algorithm has a probability of never terminating, which can be proven using
    the fundamental theorem of arithmetic: every integer greater than 1 either is a prime number 
    itself or can be represented as the product of prime numbers and that, moreover, 
    this representation is unique, up to (except for) the order of the factors.

    The thought process is:
    - 7 requires 7 possible results, but 5 only gives me 5.
    - therefore, I need to throw at least twice (ie. call rand5() twice)
    - However, throwing twice gives us 5^2 = 25 possible results, taking the modulo
    of each does NOT give us evenly probable results. 
    - Hence, I need to find a number n where 5^n is divisible by 7.
    - But, that is not possible because that means that if it was divisible by 7, all of the prime factors were to be 5, 
    which could not include 7. 
    - This concludes that there does not exist such a solution that is guaranteed to terminate.
    '''
    i, j = rand5(), rand5()
    result = (i-1)*5 + j

    while result > 21:
        i, j = rand5(), rand5()
        result = (i-1)*5 + j
    return result % 7 + 1


print('Rolling 7-sided die...')
print(rand7())
