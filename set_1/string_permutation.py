from collections import deque
class Solution(object):
    def __init__(self, string): 
        self.chars = [char for char in string]
        self.permutations = set()

    def get_permutations(self):
        dq = deque(self.chars)
        print(self.__get_permutations(dq))

    def __get_permutations(self, dq):
        if len(dq) == 1: return [dq[0]]
        if len(dq) == 2: return [''.join([dq[0], dq[1]]), ''.join([dq[1], dq[0]])]

        perms = []
        for _ in range(len(dq)):
            current = dq.popleft()
            rest = self.__get_permutations(dq)
            for substr in rest: perms.append(current + substr)
            dq.append(current)
        
        return perms

def main():
    Solution('abcd').get_permutations()

if __name__ == '__main__': main()
