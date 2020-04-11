import unittest

class QueueTwoStacks(object):
    def __init__(self):
        self.stack_1, self.stack_2 = [], []

    # Implement the enqueue and dequeue methods
    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if not len(self.stack_1) and not len(self.stack_2): raise Exception('cannot dequeue an empty queue.')
        if len(self.stack_1) == 1 and len(self.stack_2) == 0: return self.stack_1.pop()
        if len(self.stack_1) and len(self.stack_2) == 0: 
            while len(self.stack_1): self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
        if len(self.stack_2) != 0: return self.stack_2.pop()

class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()

if __name__ == "__main__":
     unittest.main()
