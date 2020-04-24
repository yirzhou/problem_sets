import random


def rand5():
    return random.randint(1, 5)

def rand7():
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


print('Rolling 7-sided die...')
print(rand7())
