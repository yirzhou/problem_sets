class MyHashSet:
    """#705. Design a HashSet without using any built-in hash table libraries.

    To be specific, your design should include these functions:

    1. add(value): Insert a value into the HashSet. 
    2. contains(value) : Return whether the value exists in the HashSet or not.
    3. remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = [False]*1000001

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return self.hashset[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
