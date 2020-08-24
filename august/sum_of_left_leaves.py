# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    """#404. Find the sum of all left leaves in a given binary tree."""
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = deque([(root, False)])
        leftsum = 0
        
        while len(q):
            node, is_left = q.popleft()
            if self.is_leaf(node) and is_left: leftsum += node.val
            
            if node.left: q.append((node.left, True))
            if node.right: q.append((node.right, False))
        return leftsum
        
        
    def is_leaf(self, node):
        return not(node.left or node.right)
        