from collections import deque, defaultdict
class Solution:
    """#127: Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
    1. Only one letter can be changed at a time.
    2. Each transformed word must exist in the word list.
    """
    def ladderLength(self, beginWord, endWord, wordList):
        """BFS Approach: remember - BFS ALWAYS finds the shortest path.
        - Time: O(k^(2)*N), where k is the length of each word, N is the number of words
        - Space: O(k^(2)*N) for storing the graphs
        """
        words = set(wordList)
        words.add(beginWord)
        L = len(beginWord)
        
        if endWord not in words: return 0
        graph, reps = self.build_graph(words, L)
        
        visited = set(beginWord)
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, dist = queue.popleft()
            visited.add(word)
            
            for rep in reps[word]:
                if endWord in graph[rep]: return dist+1
                for neighbor in graph[rep]:
                    if neighbor not in visited: 
                        queue.append((neighbor, dist+1))
                graph[rep].clear()
        return 0    

    def build_graph(self, words, L):
        graph = defaultdict(set)
        reps = defaultdict(set)
        for word in words:
            for i in range(L):
                rep = word[:i]+"*"+word[i+1:]
                reps[word].add(rep)
                graph[rep].add(word)
        return graph, reps
