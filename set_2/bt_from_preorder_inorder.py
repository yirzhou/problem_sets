class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        return

    def build_tree(self, preorder, inorder):
        n = len(preorder)
        in_index, pre_index = 0, 1
        popped = False
        
        root = TreeNode(preorder[0])
        current = root
        stack = [current]
        
        while pre_index < n:
            if len(stack) and stack[-1].val == inorder[in_index]:
                current = stack.pop()
                popped = True
                in_index += 1
            else:
                if popped:
                    current.right = TreeNode(preorder[pre_index])
                    current = current.right
                    popped = False
                else:
                    current.left = TreeNode(preorder[pre_index])
                    current = current.left
                pre_index += 1
                stack.append(current)
        
        return root

    def build(self, preorder, inorder):
        '''A recursive solution.
        '''
        root = None
        return self.__construct(root, 0, len(preorder)-1, 0, len(inorder)-1, preorder, inorder)

    def __construct(self, current, pre_begin, pre_end, in_begin, in_end, preorder, inorder):

        current = TreeNode(preorder[pre_begin])
        if in_begin == in_end: return current

        next_bound = self.__find_next_bound(in_begin, current.val, inorder)
        if preorder[pre_begin] != inorder[in_begin]:
            current.left = self.__construct(current.left, pre_begin + 1, pre_begin + next_bound, in_begin, in_begin + next_bound - 1, preorder, inorder)
        if pre_begin + next_bound + 1 <= pre_end:
            current.right = self.__construct(current.right, pre_begin + next_bound + 1, pre_end, in_begin + next_bound + 1, in_end, preorder, inorder)
        return current

    def __find_next_bound(self, in_begin, target, inorder):
        i = 0
        while inorder[in_begin + i] != target: i += 1
        return i

Solution().build_tree([1,2], [2,1])