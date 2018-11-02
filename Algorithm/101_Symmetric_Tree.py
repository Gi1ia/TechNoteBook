# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Time: O(h)
        # Space: O(log n)
        if not root:
            return True
        
        return self.compare(root.left, root.right)
        
    
    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        if left.val == right.val:
            outter = self.compare(left.left, right.right)
            inner = self.compare(left.right, right.left)
            return outter and inner
        
        return False