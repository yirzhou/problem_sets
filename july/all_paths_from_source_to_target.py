class Solution:
    """#797. Given a directed, acyclic graph of N nodes.  
    Find all possible paths from node 0 to node N-1, and return them in any order.

    The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1. 
    graph[i] is a list of all nodes j for which the edge (i, j) exists.
    """
    def allPathsSourceTarget(self, graph):
        paths = []
        tmp = []
        target = len(graph) - 1
        self.dfs(graph, 0, tmp, paths, target)
        return paths
        
    def dfs(self, graph, current, tmp, paths, target):
        tmp.append(current)
        if current == target: paths.append(tmp.copy())
        else:
            for node in graph[current]: self.dfs(graph, node, tmp, paths, target)
        tmp.pop()
