from TreeNode import TreeNode

class Solution(object):
    def __init__(self): return

    def post_order_recursive(self, root):
        if root.left: self.post_order_recursive(root.left)
        if root.right: self.post_order_recursive(root.right)
        print('current (recursive):', root.val)
        return

    def post_order_iterative_two_stacks(self, root):
        stack1, stack2 = [], []
        stack1.append(root)

        while len(stack1):
            current = stack1.pop()
            stack2.append(current)
            if current.left: stack1.append(current.left)
            if current.right: stack1.append(current.right)
        
        while len(stack2):
            current = stack2.pop()
            print('current (iterative):', current.val)

    def post_order_iterative(self, root):
        stack, visited = [root], set()

        while len(stack):
            current = stack[len(stack)-1]
            if current.left and current.left not in visited: stack.append(current.left)
            elif current.right and current.right not in visited: stack.append(current.right)
            else:
                print('current (iterative):', current.val)
                stack.pop()
                visited.add(current)
        
def main():
    root = TreeNode(4)
    root.left, root.left.left, root.left.right = TreeNode(2), TreeNode(1), TreeNode(3)
    root.right, root.right.right = TreeNode(5), TreeNode(6)
    Solution().post_order_iterative(root)
    print('- '*50)
    Solution().post_order_recursive(root)

if __name__ == '__main__': main()
