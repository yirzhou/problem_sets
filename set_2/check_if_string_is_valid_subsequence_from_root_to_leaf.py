class Solution:
    '''Given a binary tree where each path going from the root to any leaf form a valid sequence, 
    check if a given string is a valid sequence in such binary tree. 
    '''
    def is_valid_sequence(self, root, arr) -> bool:
        '''The interative solution using in-order traversal.
        - Time: O(N) in the worst case
        - Space: O(N) in the worst case
        '''
        stack = [(root, 0)]
        while len(stack):
            (node, depth) = stack.pop()
            if depth < len(arr) and arr[depth] == node.val: 
                if self.__is_leaf(node) and depth == len(arr)-1: return True
                else: 
                    if node.right and depth+1 < len(arr) and node.right.val == arr[depth+1]:
                        stack.append((node.right, depth+1))
                    if node.left and depth+1 < len(arr) and node.left.val == arr[depth+1]:
                        stack.append((node.left, depth+1))
        return False
        
    def __dfs(self, node, arr, index) -> bool:
        '''The recursive solution using in-order traversal.
        - Time: O(N) in the worst case
        - Space: O(N) in the worst case
        '''
        if not node or index > len(arr)-1 or arr[index] != node.val: return False
        if self.__is_leaf(node) and index == len(arr)-1: return True
        
        found_in_left, found_in_right = False, False
        if node.left: found_in_left = self.__dfs(node.left, arr, index+1)
        if node.right: found_in_right = self.__dfs(node.right, arr, index+1)
        
        return found_in_left or found_in_right
        
    def __is_leaf(self, node):
        return not (node.left or node.right)
