class Solution:
    '''Given a non-empty binary tree, find the maximum path sum.

    A path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 

    The path must contain at least one node and does not need to go through the root.
    '''
    def __init__(self): self.cur_max = float('-inf')
    
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
    