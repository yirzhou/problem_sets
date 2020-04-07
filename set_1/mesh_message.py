import heapq
import unittest
from collections import deque

def get_path(networks, src, dest):
    """This implementation uses BFS: BFS always find the shortest path the quickest.
    - space complexity: O(N) where N is the number of nodes
    - time complexity: O(N + M), where M is the total number of neighbors. There are E edges and in total we 
    visit all edges, meaning that we visit 2M neighbors in total.
    """
    if src not in networks or dest not in networks: raise ValueError('invalid input')
    has_path_to = {}

    stack = []

    stack.append(src)
    while len(stack):
        current = stack.pop()
        if current in networks:
            for neighbor in networks[current]:
                if neighbor not in has_path_to:
                    stack.append(neighbor)
                    has_path_to[neighbor] = current
    
    path = deque()
    if dest in has_path_to:
        path.appendleft(dest)
        while dest != src:
            dest = has_path_to[dest]
            path.appendleft(dest)
        return list(path)
    return None

def shortest_path(network, src, dest):
    """Remember: both BFS and DFS will eventually find a path if one exists. The difference between the two is:
    - BFS always finds the shortest path.
    - DFS usually uses less space.
    """
    
    if src not in network or dest not in network: raise ValueError('invalid src/dest')
    if dest in src and dest == src: return [src]
    if dest in src: return [src, dest]
    vector_table = {}
    visited = set()
    priority_queue = []
    # initialize vector table
    for neighbor in network[src]:
        vector_table[neighbor] = (1, neighbor)
        heapq.heappush(priority_queue, (1, neighbor))
        
    while len(priority_queue):
        cost, current_node = heapq.heappop(priority_queue)
        if current_node == dest: break
        if current_node in visited: continue
        visited.add(current_node) 

        # visit all of the neighbors
        for neighbor in network[current_node]:
            if neighbor in vector_table:
                new_cost = cost + 1
                if new_cost < vector_table[neighbor][0]:
                    vector_table[neighbor] = (new_cost, neighbor)
                    heapq.heappush(priority_queue, (new_cost, neighbor))
            else: 
                vector_table[neighbor] = (cost+1, current_node)
                heapq.heappush(priority_queue, (cost+1, neighbor))

    q = deque()
    next_hop = dest
    if next_hop in vector_table:
        while next_hop != vector_table[next_hop][1]: 
            q.appendleft(next_hop)
            _, next_hop = vector_table[next_hop]
        q.appendleft(next_hop)
        if next_hop != src: q.appendleft(src)
        return list(q)
    else:
        return None

# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')

unittest.main(verbosity=2)
