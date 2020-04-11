from TreeNode import TreeNode

class Solution(object):
    def __init__(self): return

    def pre_order_recursive(self, root):
        print('current (recursive):', root.val)
        if root.left: self.pre_order_recursive(root.left)
        if root.right: self.pre_order_recursive(root.right)
        return

    def pre_order_iterative(self, root):
        stack = [root]

        while len(stack):
            current = stack.pop()
            print('current (iterative):', current.val)

            if current.right: stack.append(current.right)
            if current.left: stack.append(current.left)

def main():
    root = TreeNode(4)
    root.left, root.left.left, root.left.right = TreeNode(2), TreeNode(1), TreeNode(3)
    root.right, root.right.right = TreeNode(5), TreeNode(6)
    Solution().pre_order_iterative(root)
    print('- '*50)
    Solution().pre_order_recursive(root)

if __name__ == '__main__': main()
