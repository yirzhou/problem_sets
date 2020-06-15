# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """#700. Given the root node of a binary search tree (BST) and a value. 
    You need to find the node in the BST that the node's value equals the given value. 
    Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.
    """
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        node = root
        while node is not None:
            if val == node.val:
                return node
            elif val < node.val:
                node = node.left
            else:
                node = node.right
        return None
        