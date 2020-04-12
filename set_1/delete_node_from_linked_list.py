import unittest

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_node_at_beginning(self):
        delete_node(self.first)
        actual = self.first.get_values()
        expected = [2, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_in_middle(self):
        delete_node(self.second)
        actual = self.first.get_values()
        expected = [1, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_at_end(self):
        with self.assertRaises(Exception):
            delete_node(self.fourth)

    def test_one_node_in_list(self):
        unique = Test.LinkedListNode(1)
        with self.assertRaises(Exception):
            delete_node(unique)

def delete_node(node):
    '''Given only a pointer to that node, the deletion
    can be done in constant time!

    But, there are two potential side-effects:

    1. Any references to the input node have now effectively been reassigned to its next node. 
        In our example, we "deleted" the node assigned to the variable b, but in actuality we just gave it a new value (2) and a new next! 
        If we had another pointer to b somewhere else in our code and we were assuming it still had its old value (8), that could cause bugs.
    2. If there are pointers to the input node's original next node, 
        those pointers now point to a "dangling" node (a node that's no longer reachable by walking down our list). 
    '''
    next_node = node.next
    if next_node:
        node.value = next_node.value
        node.next = next_node.next
    else: raise Exception('invalid input')

unittest.main(verbosity=2)
 