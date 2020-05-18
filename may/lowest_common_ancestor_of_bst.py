
class Solution:
    """#235. Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST."""
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """DFS Approach:
        The main idea is to track the parent node of each node. 
        Then, starting from a node itself (p or q), looking for the first common ancestor.
        - Time: O(N) in worst case
        - Space: O(N)
        """
        parents = {}
        parents[root] = None
        stack = [root]
        
        while (p not in parents or q not in parents):
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
        
        p_ancestor = p
        p_ancestors = set()
        
        while p_ancestor:
            p_ancestors.add(p_ancestor)
            p_ancestor = parents[p_ancestor]
        
        lcm = q
        while lcm not in p_ancestors: lcm = parents[lcm]
        
        return lcm
            