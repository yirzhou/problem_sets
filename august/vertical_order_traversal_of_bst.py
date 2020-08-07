# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import operator
import collections
import bisect
class Solution:
    """#987. Given a binary tree, return the vertical order traversal of its nodes values.

    For each node at position (X, Y), its left and right children respectively will be at positions (X-1, Y-1) and (X+1, Y-1).

    Running a vertical line from X = -infinity to X = +infinity, whenever the vertical line touches some nodes, we report the values of the nodes in order from top to bottom (decreasing Y coordinates).

    If two nodes have the same position, then the value of the node that is reported first is the value that is smaller.

    Return an list of non-empty reports in order of X coordinate.  Every report will have a list of values of nodes.
    """
    def verticalTraversal(self, root: TreeNode):
        cache=collections.defaultdict(list)
        def helper(node, x=0, y=0):
            if node is None: return
            bisect.insort(cache[x], (-y, node.val))
            helper(node.left, x - 1, y - 1)
            helper(node.right, x + 1, y - 1)
            return cache
        return [[tup[1] for tup in v] for k, v in sorted(helper(root).items())]
