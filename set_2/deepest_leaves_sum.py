from queue import Queue

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def is_leaf(self):
        return not(self.left or self.right)

class Solution:
    """
    - I should be able to achieve the same goal iteratively or recursively.
    - I should also be able to achieve the same goal using BFS or DFS. 
    """
    def __init__(self): return 

    def deepest_leaves_sum(self, root):
        """DFS Approach - where we can get the leaves the fastest.
        """
        max_height, max_sum = 0, 0
        (current, node_height) = (root, 0)
        stack = []
        while len(stack) or current:
            if current:
                stack.append((current, node_height))
                if current.is_leaf():
                    if node_height > max_height:
                        max_height = node_height
                        max_sum = current.val
                    elif node_height == max_height: max_sum += current.val
                current = current.left
                node_height += 1
            else:
                current, node_height = stack.pop()
                current = current.right
                node_height += 1
        
        return max_sum

    def deepest_leaves_sum_bfs(self, root):
        """BFS Approach - where we can get all nodes at the same height.
        """

        current_sum, max_sum, children_count = 0, 0, 0
        level_signal = 1
        q = Queue()
        q.put(root)

        while not q.empty():
            node = q.get()
            level_signal -= 1

            if node.left: 
                q.put(node.left)
                children_count += 1
            if node.right: 
                q.put(node.right)
                children_count += 1

            if node.is_leaf(): current_sum += node.val
            if level_signal == 0:
                max_sum = current_sum
                current_sum = 0
                level_signal, children_count = children_count, 0
        
        return max_sum

    
def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.left.left = TreeNode(7)
    root.right.right = TreeNode(6)
    root.right.right.right = TreeNode(8)
    print(Solution().deepest_leaves_sum_bfs(root))

if __name__ == '__main__': main()