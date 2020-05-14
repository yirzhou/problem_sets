class BinaryTreeNode(object):
    """Write a function to see if a binary tree is "superbalanced" (a new tree property we just made up).
    """
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right