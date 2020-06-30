class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.word = None
        
    def has_letter(self, char):
        return self.children[ord(char)-97] is not None
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            idx = ord(char)-97
            if not node.children[idx]: node.children[idx] = TrieNode()
            node = node.children[idx]
        node.word = word
    
class Solution:
    """#212. Given a 2D board and a list of words from the dictionary, find all words in the board.

    Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
    
    The same letter cell may not be used more than once in a word.
    """
    def __init__(self):
        self.dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        
    def findWords(self, board, words):
        words_found = []
        if len(words) == 0 or len(board) == 0 or len(board[0]) == 0: return words_found
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        trie = Trie()
        for word in words: trie.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if trie.root.has_letter(board[i][j]):
                    idx = ord(board[i][j])-97
                    self.search(board, trie.root.children[idx],i,j,visited,words_found)
        return words_found
    
    def search(self, board, node, i, j, visited, words_found):
        if node.word is not None: 
            words_found.append(node.word)
            node.word = None
        
        visited[i][j] = True
        for (r,c) in self.dirs:
            row, col = i+r, j+c
            if (0 <= row < len(board) and 0 <= col < len(board[0]) and not visited[row][col] and node.has_letter(board[row][col])):
                self.search(board, node.children[ord(board[row][col])-97], row, col, visited, words_found)
        visited[i][j] = False
        