from collections import deque

class Solution:
    """We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
    Return true if and only if the nodes corresponding to the values x and y are cousins.
    """
    def is_cousins(self, root: TreeNode, x: int, y: int) -> bool:
        """BFS Solution"""
        if root.val == x or root.val == y: return False
        q = deque([(root, None, 0)])
        height1, p1 = None, None
        
        while len(q):
            (node, parent, height) = q.popleft()
            if height1 is not None and height>height1: return False
            
            if (node.val == x or node.val == y) and height1 is None: height1, p1 = height, parent.val
            elif (node.val == x or node.val == y) and height1 is not None: return height == height1 and parent.val != p1
            
            if node.left: q.append((node.left, node, height+1))
            if node.right: q.append((node.right, node, height+1))
        
        return False
