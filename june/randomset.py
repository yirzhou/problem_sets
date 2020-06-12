from collections import defaultdict
import random
class RandomizedSet:
    """#380. Design a data structure that supports all following operations in average O(1) time.

    1. insert(val): Inserts an item val to the set if not already present.
    2. remove(val): Removes an item val from the set if present.
    3. getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.indices = defaultdict(int)
        self.deleted = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.indices and val not in self.deleted: return False
        
        if val in self.deleted: 
            self.deleted.remove(val)
            self.l[self.indices[val]] = val
        else:
            self.indices[val] = len(self.l)
            self.l.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.deleted or val not in self.indices: return False
        self.deleted.add(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        index = random.randint(0, len(self.l)-1)
        while self.l[index] in self.deleted:
            index = random.randint(0, len(self.l)-1)
        return self.l[index]
