import random


def rand7():
    return random.randint(1, 7)


def rand5():
    '''Simply re-roll each time I get a number larger than 5.
    Worst case: infinite time.
    '''
    result = rand7()
    if result > 5: result = rand7()
    return result

def wrong_rand5():
    '''This is my naive solution...
    Although the partitions are equally spaced out,
    the probability of getting into each partition is not constant.
    '''
    rand = rand7()*5
    if 1 <= rand <= 7: return 1
    if 8 <= rand <= 14: return 2
    if 15 <= rand <= 21: return 3
    if 22 <= rand <= 28: return 4
    return 5


print('Rolling 5-sided die...')
print(rand5())