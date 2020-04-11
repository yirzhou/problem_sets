import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left, self.right = None, None


class Solution:
    def __init__(self): self.diameter = 0

    def diameter_of_binary_tree(self, root):
        if not root: return 0

        self.diameter = 0
        # self.__dfs_recursive(root, 0)
        self.__dfs_iterative(root)

        return self.diameter

    def __dfs_recursive(self, node, height):
        '''This is the recursive solution.
        - Time: O(N) on average where N is the total number of nodes since it needs to visit every node.
        - Space: O(lg(N)) on average, O(N) in worst case.
        '''

        if not node.left and not node.right: return height

        left_height, right_height = 0, 0

        if node.left:
            left_height = self.__dfs_recursive(node.left, 1)
        if node.right:
            right_height = self.__dfs_recursive(node.right, 1)

        self.diameter = max(self.diameter, right_height + left_height)
        return height + max(left_height, right_height)
    
    def __dfs_iterative(self, node):
        '''This is the iterative approach. 
        - Time: O(N)
        - Space: O(N)
        The idea is to use post-order traversal so that the left and right must have been both visited.
        '''
        stack = []
        depths = {}

        if node: stack.append(node)
        while len(stack):
            current = stack[len(stack)-1]
            if current.left and current.left not in depths: stack.append(current.left)
            elif current.right and current.right not in depths: stack.append(current.right)
            else:
                stack.pop()
                left_depth, right_depth = depths.get(current.left, 0), depths.get(current.right, 0)
                depths[current] = max(left_depth, right_depth) + 1
                self.diameter = max(self.diameter, left_depth + right_depth)
    
class Test(unittest.TestCase):

    def test_left_deeper(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)

        actual = Solution().diameter_of_binary_tree(root)
        self.assertEqual(actual, 3)
    
    def test_same_depth(self):
        root = TreeNode(1)
        root.left, root.left.left = TreeNode(2), TreeNode(4)
        root.right, root.right.right = TreeNode(3), TreeNode(5)
        actual = Solution().diameter_of_binary_tree(root)
        self.assertEqual(actual, 4)

unittest.main(verbosity=2)

# def main():
#     root = TreeNode(1)
#     root.left = TreeNode(2)
#     root.left.left = TreeNode(4)
#     root.left.right = TreeNode(5)
#     root.right = TreeNode(3)
#     Solution().diameter_of_binary_tree(root)

# if __name__ == '__main__': main()
    