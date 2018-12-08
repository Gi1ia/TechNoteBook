# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST_inorder(self, root):
        # Inorder pattern
        # ref: https://leetcode.com/problems/validate-binary-search-tree/discuss/32112/Learn-one-iterative-inorder-traversal-apply-it-to-multiple-tree-questions-(Java-Solution)
        if not root:
            return True
        
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if pre and root.val < pre.val:
                return False
            
            pre = root
            root = root.right
        
        return True

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
        
        