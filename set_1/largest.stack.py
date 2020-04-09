class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

class MaxStack(object):
    """It takes O(1) to get the max value in the stack.
    Albeit it requires O(m) extra space where m is the number of operations.
    """
    def __init__(self):
        self.stack = Stack()
        self.maxes = Stack()

    def push(self, item):
        self.stack.push(item)

        if not self.maxes.peek() or self.maxes.peek() <= item: self.maxes.push(item)

    def pop(self):
        item = self.stack.pop()
        
        if self.maxes.peek() and self.maxes.peek() == item: self.maxes.pop()
        return item

    def get_max(self):
        return self.maxes.peek()
