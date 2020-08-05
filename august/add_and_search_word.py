class WordDictionary:
    """#211. Design a data structure that supports the following two operations:

    - void addWord(word)
    - bool search(word)
    search(word) can search a literal word or a regular expression string containing only letters a-z or ".". 
    
    A "." means it can represent any one letter.
    """
    class Trie(object):
        def __init__(self):
            self.children = {}
            self.is_word = False
            
    def __init__(self):
        self.root = self.Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children: node.children[c] = self.Trie()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.root, word)

    def searchNode(self, node, word: str) -> bool:
        for i, c in enumerate(word):
            if c == '.':
                return any(self.searchNode(node.children[w], word[i+1:]) for w in node.children)
            if c not in node.children: return False
            node = node.children[c]
        return node.is_word
