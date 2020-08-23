from collections import deque
class Trie:
    def __init__(self):
        self.Trie = {}

    def insert(self, word):
        curr = self.Trie
        for w in word:
            if w not in curr:
                curr[w] = {}
            curr = curr[w]
        curr['#'] = 1

    def search(self, word):
        curr = self.Trie
        for w in word:
            if w not in curr:
                return False
            if "#" in curr[w]:
                return True
            curr = curr[w]
        return False

class StreamChecker:
    """#1032. Implement the StreamChecker class as follows:
    * StreamChecker(words): Constructor, init the data structure with the given words.
    * query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
    """
    def __init__(self, words):
        self.trie = Trie()
        self.stream = deque([])

        for word in set(words):
            self.trie.insert(word[::-1])

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        return self.trie.search(self.stream)
