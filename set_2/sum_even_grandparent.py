from queue import Queue
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self): return 

    def sum_even_grandparent(self, root):
        """I will use bfs and sum everything along the way
        """
        return self.__sum_even_grandparent(root)

    def __sum_even_grandparent(self, root):
        height = 0
        q = Queue()
        q.put((root, None))
        childrens, nodes_to_visit = 0, 1
        sum_even_gp = 0

        while not q.empty():
            node, parent = q.get()
            nodes_to_visit -= 1

            if node.left:
                # check its child and its parent (the child's grandparent)
                if parent and parent.val % 2 == 0: sum_even_gp += node.left.val
                childrens += 1
                q.put((node.left, node))
            if node.right:
                if parent and parent.val % 2 == 0: sum_even_gp += node.right.val
                childrens += 1
                q.put((node.right, node))

            if nodes_to_visit == 0:
                height += 1
                nodes_to_visit = childrens
                childrens = 0
        return sum_even_gp


def main():
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(5)
    print(Solution().sum_even_grandparent(root))

if __name__ == '__main__': main()
