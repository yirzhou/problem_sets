class CombinationIterator:
    """#1286. Design an Iterator class, which has:

    - A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
    - A function next() that returns the next combination of length combinationLength in lexicographical order.
    - A function hasNext() that returns True if and only if there exists a next combination.
    """
    
    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.length = len(characters)
        self.combos = self.__get_combos(combinationLength)
        self.ind = len(self.combos)-1

    def next(self) -> str:
        s = ""
        for i in range(self.length):
            if self.combos[self.ind][i] != "0":
                s += self.chars[i]
        self.ind -= 1
        return s

    def hasNext(self) -> bool:
        return self.ind > -1
        
    def __get_combos(self, length):
        end = int("1"*self.length,2)
        combos = []
        for i in range(end+1):
            b = bin(i)[2:]
            if b.count('1') == length: combos.append(b.zfill(self.length))
        return combos

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
