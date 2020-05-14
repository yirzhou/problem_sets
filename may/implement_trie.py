class Trie:
    """Implement a trie with insert, search, and startsWith methods."""
    class Node(object):
        def __init__(self):
            self.is_word = False
            self.children = {}

    def __init__(self):
        self.node = self.Node()

    def insert(self, word: str) -> None:
        cur = self.node
        for letter in word:
            if letter not in cur.children: cur.children[letter] = self.Node()
            cur = cur.children[letter]
        
        cur.is_word = True
        
    def search(self, word: str) -> bool:
        cur = self.node
        for letter in word:
            if letter not in cur.children: return False
            cur = cur.children[letter]
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.node
        for letter in prefix:
            if letter not in cur.children: return False
            cur = cur.children[letter]
        return True
