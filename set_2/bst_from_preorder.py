class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.root = None
        
    def bst_from_preorder(self, preorder):
        n = len(preorder)
        if not n:
            return None
        
        root = TreeNode(preorder[0])         
        stack = [root, ] 
        
        for i in range(1, n):
            node, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val: 
                node = stack.pop()
             
            if node.val > child.val:
                node.left = child 
            else:
                node.right = child 
            stack.append(child)
        return root
        

Solution().bst_from_preorder([8,5,1,7,10,12])