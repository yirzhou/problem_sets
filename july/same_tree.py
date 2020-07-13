# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    """#100. Given two binary trees, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
    """
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if ((not p) and q) or (p and (not q)): return False
        if (not p) and (not q): return True
        
        queue_p, queue_q = deque([p]), deque([q])
        
        while len(queue_p) and len(queue_q):

            node_p, node_q = queue_p.popleft(), queue_q.popleft()
            if not self.is_similar(node_p, node_q): return False
            
            if node_p.val != node_q.val: return False
            
            if node_p.left: queue_p.append(node_p.left)
            if node_p.right: queue_p.append(node_p.right)
            if node_q.left: queue_q.append(node_q.left)
            if node_q.right: queue_q.append(node_q.right)
        
        return len(queue_p) == 0 and len(queue_q) == 0    
    
    def is_similar(self, p, q):
        if p.left and p.right: return q.left and q.right
        if p.left and not p.right: return q.left and (not q.right)
        if p.right and not p.left: return q.right and not(q.left)
        
        return (not q.left) and (not q.right)
        