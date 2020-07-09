# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """Given a binary tree, write a function to get the maximum width of the given tree. 
    The width of a tree is the maximum width among all levels. 
    The binary tree has the same structure as a full binary tree, but some nodes are null.

    The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level,
    where the null nodes between the end-nodes are also counted into the length calculation.
    """
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = [(root, 0, 0)]
        cur_depth = left = max_depth = 0
        for node, depth, pos in q:
            if node:
                q.append((node.left, depth+1, pos*2))
                q.append((node.right, depth+1, pos*2 + 1))
                if cur_depth != depth:
                    cur_depth = depth
                    left = pos
                max_depth = max(pos - left + 1, max_depth)
        return max_depth
