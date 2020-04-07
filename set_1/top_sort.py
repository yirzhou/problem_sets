from collections import deque

class Graph(object):
    def __init__(self):
        self.edges = {}
        self.nodes = set()
        self.visited = set()
        self.in_degrees = {}

    def add_edge(self, a, b):
        if a not in self.edges:
            self.edges[a] = set()
        self.edges[a].add(b)

        if a not in self.in_degrees: self.in_degrees[a] = 0
        if b not in self.in_degrees: self.in_degrees[b] = 0
        self.in_degrees[b] += 1

        self.nodes.add(a)
        self.nodes.add(b)

    def get_neighbors(self, node):
        if node not in self.nodes:
            raise ValueError('invalid node')
        return self.edges[node]
    
    def is_visited(self, node):
        return node in self.visited

    def initial_nodes(self):
        nodes = []
        for node in self.in_degrees:
            if self.in_degrees[node] == 0: nodes.append(node)
        return nodes

    def topological_sort(self):
        
        stack = self.initial_nodes()
        
        topological_order = []
        while len(stack):
            current = stack.pop()
            topological_order.append(current)
            if current in self.edges:
                for neighbor in self.edges[current]:
                    self.in_degrees[neighbor] -= 1
                    if self.in_degrees[neighbor] == 0: stack.append(neighbor)

        return topological_order

def main():
    graph = Graph()
    graph.add_edge('c', 'b')
    graph.add_edge('c', 'a')
    graph.add_edge('b', 'd')
    graph.add_edge('a', 'd')
    graph.add_edge('e', 'a')
    graph.add_edge('e', 'd')
    graph.add_edge('d', 'g')
    graph.add_edge('e', 'f')
    graph.add_edge('d', 'h')
    graph.add_edge('h', 'j')
    graph.add_edge('h', 'i')
    graph.add_edge('g', 'i')
    graph.add_edge('i', 'l')
    graph.add_edge('j', 'l')
    graph.add_edge('j', 'm')
    graph.add_edge('f', 'j')
    graph.add_edge('f', 'k')
    graph.add_edge('k', 'j')
    print(graph.topological_sort())

if __name__ == '__main__':
    main()