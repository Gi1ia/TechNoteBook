# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        values = self.dfs(root)
        
        return max(values[0], values[1])
    
    def dfs(self, node):
        """
        return val: tuple(int, int)
        val[0]: How many value do I earn while roobing the node
        val[1]: Not rob node
        """
        if not node:
            return (0, 0)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        rob_node = left[1] + right[1] + node.val
        not_rob = max(left[0], left[1]) + max(right[0], right[1])
        
        return (rob_node, not_rob)
        
        