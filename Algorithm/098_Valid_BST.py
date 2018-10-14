# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self._isValidBST(root, float("-inf"), float("inf"))
    
    def _isValidBST(self, node, left, right):
        if not node:
            return True
        
        if not left < node.val < right:
            return False
    
        return self._isValidBST(node.left, left, node.val) and self._isValidBST(node.right, node.val, right)
        
        