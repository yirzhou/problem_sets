# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """#129. Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers.
    """
    def __init__(self):
        self.sum = 0
        
    def sumNumbers(self, root: TreeNode) -> int:
        """DFS approach:
        - Time: O(N).
        - Space: O(h) where h is the deepest depth of the tree.
        """
        if root:
            self.dfs(root, [])
        return self.sum
        
    def dfs(self, node, digits):
        digits.append(node.val)
        if self.is_leaf(node):
            self.sum += self.reduce(digits)
        else:
            if node.left:
                self.dfs(node.left, digits)
            if node.right:
                self.dfs(node.right, digits)
        digits.pop()
    
    def is_leaf(self, node):
        return (not node.left) and (not node.right)

    def reduce(self, digits):
        return int("".join(map(str, digits))) 
        