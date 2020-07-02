# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    """#107. Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
    (ie, from left to right, level by level from leaf to root).
    """
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque([(root,0)])
        
        cur_height = 0
        nodes = []
        
        res = deque()
        
        while len(queue):
            node, height = queue.popleft()
            
            if cur_height != height:
                res.appendleft(nodes.copy())
                cur_height = height
                nodes = []
            nodes.append(node.val)
            
            if node.left:
                queue.append((node.left, height+1))
            if node.right:
                queue.append((node.right, height+1))
        
        if len(nodes): res.appendleft(nodes.copy())
        return res
    