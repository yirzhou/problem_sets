from collections import deque
class Solution:
    """#103. Given a binary tree, return the zigzag level order traversal of its nodes' values. 
    (ie, from left to right, then right to left for the next level and alternate between).
    """
    def zigzagLevelOrder(self, root):
        if not root: return []
        q = deque([root])
        result, direction = [], 1
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            result.append(level[::direction])
            direction *= (-1)
        return result
