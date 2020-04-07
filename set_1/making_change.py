class Solution(object):
    def __init__(self):
        self.coins = []
        self.sums = {}
        self.possibilities = []

    def change_possibilities(self, amount, denominations):
        self.coins = [denomination for denomination in denominations]
        self.__change_combos(0, amount, [])
        return len(self.possibilities)

    def change_possibilities_mem(self, amount, denominations):
        mem = [0]*(amount+1)
        mem[0] = 1
        for denom in denominations:
            for i in range(denom, amount+1):
                if i == denom: mem[i] += 1
                elif denom <= i: mem[i] += mem[i-denom]
        return mem[amount]

    def __change_combos(self, begin, target, stack):
        """A recursive top-bottom approach.
        - O(N) space (call stack) where N is the number of amount of money
        - O(N*M) time where M is the number of coins
        """
        if target == 0: 
            self.possibilities.append(stack.copy())
            return 
        if target < 0: return 

        for i in range(begin, len(self.coins)):
            coin = self.coins[i]
            stack.append(coin)
            self.__change_combos(i, target-coin, stack)
            stack.pop()
        return 
    
    def __combine_list(self, combo, stack):
        for item in stack:
            for elem in combo: item.append(elem)

def main():
    solution = Solution()
    possibilities = solution.change_possibilities(4, (1,2,3))
    print(possibilities)
    solution.change_possibilities_mem(5, (1,2))

if __name__ == '__main__': main()