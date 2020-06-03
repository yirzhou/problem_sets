# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    """#226. Invert a binary tree."""
    def invertTree(self, root: TreeNode) -> TreeNode:
        """BFS Approach:
        - Time: O(N)
        - Space: O(N)
        """
        if root == None: return root
        queue = deque([root])
        
        while len(queue) != 0:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
