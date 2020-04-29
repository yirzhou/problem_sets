class Solution:
    '''Given a non-empty binary tree, find the maximum path sum.

    A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 

    The path must contain at least one node and does not need to go through the root.
    '''
    def __init__(self): self.cur_max = float('-inf')

    def max_path_sum_iterative(self, root):
        '''The iterative approach using similar logic.
        We are still doing a post-order traversal.

        - Time: O(N)
        - Space: O(N) but not limited by the call stack
        '''
        if not root: return 0
        cur_max = float('-inf')
        stack1, stack2 = [(root, None, -1)], []
        left, right = dict(), dict()
        
        # constructing post order traversal stack 
        while len(stack1):
            (node, parent, prop) = stack1.pop()
            stack2.append((node, parent, prop))
            if node.left: stack1.append((node.left, node, 0))
            if node.right: stack1.append((node.right, node, 1))
                
        while len(stack2):
            (node, parent, prop) = stack2.pop()
            
            left_max = left.get(node, 0)
            right_max = right.get(node, 0)
            
            cur_max = max(cur_max, node.val, node.val+left_max, node.val+right_max, node.val+left_max+right_max)
            
            if parent:
                # left subtree
                if not prop: left[parent] = max(node.val, node.val+right_max, node.val+left_max)
                else: right[parent] = max(node.val, node.val+right_max, node.val+left_max)
        return cur_max 
    
    def max_path_sum(self, root: TreeNode) -> int:
        self.cur_max = float('-inf')
        self.__max_path_sum(root)
        return self.cur_max
        
    def __max_path_sum(self, node):
        '''The intuitive recursive solution.
        At each node, the current max could be one of the following:
        - current max
        - itself
        - itself + left
        - itself + right
        - itself + left + right

        When it returns to its ancestor/parent, to make a path, it returns one of the following:
        - itself
        - itself + left
        - itself + right

        Efficiency:
        - Time: O(N)
        - Space: O(lg(N)) on average, O(N) in the worst case
        '''
        if not node: return 0
        left_max = self.__max_path_sum(node.left)
        right_max = self.__max_path_sum(node.right)
        self.cur_max = max(self.cur_max, node.val, node.val+left_max, node.val+right_max, node.val+left_max+right_max)
        return max(node.val, node.val+right_max, node.val+left_max)
    