from collections import deque
class Solution:
    """#886.Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

    Each person may dislike some other people, and they should not go into the same group. 

    Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

    Return true if and only if it is possible to split everyone into two groups in this way."""
    def possibleBipartition(self, N: int, dislikes) -> bool:
        """BFS approach:
        A graph is built with the input dislikes by connecting those nodes who repel each other together.

        Then, use BFS to walk through the graph and color them with red or green. 

        For each neighbor of a node, if the node has been colored 
        and it has the same color as the current node, it cannot be partitioned.

        - Time: O(E + V)
        - Space: O(N^2) in worst case if all nodes are connected with each other. 
        """
        colors = {}
        graph = []
        for _ in range(N+1): graph.append([])
        red, green = 'R', 'G'
        
        # build the graph
        for [a,b] in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        # BFS
        queue = deque()
        for v in range(1, N+1):
            if len(graph[v]) == 0: continue
            if v in colors: continue
                
            queue.append((v, red))
            colors[v] = red
            while len(queue):
                (node, color) = queue.popleft()
                neighbors = graph[node]
                for neighbor in neighbors: 
                    if neighbor in colors:
                        if colors[neighbor] == color: return False
                    else:
                        neighbor_color = green if color == red else red
                        colors[neighbor] = neighbor_color
                        queue.append((neighbor, neighbor_color))
        return True
                    