# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_depth = 0
        return self.nodeDepth(root, max_depth)
        
    def nodeDepth(self, node: TreeNode, depth) -> int:
        if not node:
            return depth
        
        return max(self.nodeDepth(node.left, depth + 1), self.nodeDepth(node.right, depth + 1))