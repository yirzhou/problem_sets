class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """#1008. Return the root node of a binary search tree that matches the given preorder traversal."""
    def bstFromPreorder(self, preorder) -> TreeNode:
        """Iterative approach.

        - Time: O(N)
        - Space: O(N)
        """
        length = len(preorder)
        root = TreeNode(preorder[0])
        node = root
        stack = [node]
        
        ptr = 1
        while ptr < length:
            cur = preorder[ptr]
            while stack and stack[-1].val < cur:
                node = stack.pop()
            
            if cur < node.val:
                node.left = TreeNode(cur)
                node = node.left
            else:
                node.right = TreeNode(cur)
                node = node.right
            stack.append(node)
            ptr += 1
        
        return root
