# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """#222. Given a complete binary tree, count the number of nodes."""
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left_depth, right_depth = self.depth(root.left), self.depth(root.right)
        return pow(2,left_depth)+self.countNodes(root.right) if left_depth == right_depth else pow(2,right_depth)+self.countNodes(root.left)
        
    def depth(self, node):
        if not node: return 0
        return 1+self.depth(node.left)
        