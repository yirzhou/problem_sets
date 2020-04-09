class Solution(object):
    def __init__(self): return

    def backspace_compare(self, S, T):
        '''This takes O(N) time and O(N) space.
        '''
        stack = []

        for char in S:
            if char == '#' and len(stack): stack.pop()
            elif char != '#': stack.append(char)

        s_processed = ''.join(stack)

        stack.clear()

        for char in T:
            if char == '#' and len(stack): stack.pop()
            elif char != '#': stack.append(char)

        t_processed = ''.join(stack)

        return s_processed == t_processed

    def backspace_compare_reverse(self, S, T):
        '''This takes O(N) time and O(1) space.
        '''
        skipS, skipT, s, t = 0, 0, len(S)-1, len(T)-1

        while s >= 0 or t >= 0:
            while s >= 0:
                if S[s] == '#':
                    skipS += 1
                    s -= 1
                elif skipS > 0: 
                    skipS -= 1
                    s -= 1
                else: break

            while t >= 0:
                if T[t] == '#':
                    skipT += 1
                    t -= 1
                elif skipT > 0:
                    skipT -= 1
                    t -= 1
                else: break
            
            if s >= 0 and t >= 0 and S[s] != T[t]: return False
            if (s >= 0) != (t >= 0): return False
            s -= 1
            t -= 1

        return True

def main():

    S = 'a#c'
    T = 'b'
    solution = Solution()

    print(solution.backspace_compare_reverse(S, T))

if __name__ == '__main__': main()
