from TreeNode import TreeNode

class Solution(object): 
    def __init__(self): return

    def in_order_iterative(self, node):
        stack = []
        current = node

        while len(stack) or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print('current (iterative):',current.val)
                current = current.right

    def in_order_recursive(self, node):
        if node.left:
            self.in_order_recursive(node.left)
        print('current (recursive):', node.val)
        if node.right:
            self.in_order_recursive(node.right)
        return 

def main():
    root = TreeNode(4)
    root.left, root.left.left, root.left.right = TreeNode(2), TreeNode(1), TreeNode(3)
    root.right, root.right.right = TreeNode(5), TreeNode(6)
    Solution().in_order_iterative(root)
    print('- '*50)
    Solution().in_order_recursive(root)


if __name__ == '__main__': main()
