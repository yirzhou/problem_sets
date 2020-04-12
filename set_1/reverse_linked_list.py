import unittest

class Solution(object):
    def __init__(self): return

    def reverse(self, head_of_list):
        '''Reverse the linked list in place
        '''
        if not head_of_list: return head_of_list
        return self.__reverse_constant_space(head_of_list)

    def __reverse(self, node, prev, head):
        '''Reverse the linked list recursively.
        - O(N) time
        - O(N) space, which could be limited by the callstack
        '''
        if not node.next: 
            head = node
            head.next = prev
        else:
            head = self.__reverse(node.next, node, head)
            node.next = prev
        return head

    def __reverse(self, head):
        '''Reverse the linked list iteratively using a stack.
        - O(N) time
        - O(N) space (in the heap)
        '''
        current = head
        stack = [(current, None)]
        while current.next:
            prev = current
            current = current.next
            stack.append((current, prev))
        
        head, head.next = stack.pop()
        while len(stack): current, current.next = stack.pop()
        return head

    def __reverse_constant_space(self, head):
        '''Reverse the linked list iteratively.
        - O(N) time
        - O(1) space
        '''

        current = head
        prev_node = None
        while current.next:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node

        # handle the original tail
        current.next = prev_node
        head = current
        return head

# Tests

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

    def test_short_linked_list(self):
        second = Test.LinkedListNode(2)
        first = Test.LinkedListNode(1, second)

        result = Solution().reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [2, 1]
        self.assertEqual(actual, expected)

    def test_long_linked_list(self):
        sixth = Test.LinkedListNode(6)
        fifth = Test.LinkedListNode(5, sixth)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)

        result = Solution().reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [6, 5, 4, 3, 2, 1]
        self.assertEqual(actual, expected)

    def test_one_element_linked_list(self):
        first = Test.LinkedListNode(1)

        result = Solution().reverse(first)
        self.assertIsNotNone(result)

        actual = result.get_values()
        expected = [1]
        self.assertEqual(actual, expected)

    def test_empty_linked_list(self):
        result = Solution().reverse(None)
        self.assertIsNone(result)


unittest.main(verbosity=2)