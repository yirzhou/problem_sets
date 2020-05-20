# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """#230. Given a binary search tree, write a function kthSmallest to find the kth smallest element in it."""
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """In-order traversal:
        - Time: O(N) in worst case
        - Space: O(lg(N)) on average
        """
        counter = 0
        
        stack = [root]
        node = root
        kth_smallest = 0
        
        while stack or node:
            if node:
                if node.left: stack.append(node.left)
                node = node.left
            else:
                node = stack.pop()
                counter += 1
                if counter == k: 
                    kth_smallest = node.val
                    break
                if node.right: stack.append(node.right)
                node = node.right
        return kth_smallest
        