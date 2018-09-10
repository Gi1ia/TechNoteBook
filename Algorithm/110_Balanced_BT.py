# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.balanced_height(root) != -1
    
    def balanced_height(self, root):
        if not root:
            return 0
        
        # Get the value first to save time
        left_height = self.balanced_height(root.left)
        right_height = self.balanced_height(root.right)
        
        if left_height == -1:
            return -1
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
        
    def isBalanced_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        return self.isBalanced(root.left) and \
            self.isBalanced(root.right) and \
            abs(self.height(root.left) - self.height(root.right)) <= 1
        
    
    def height(self, root):
        if not root:
            return 0
        
        return 1 + max(self.height(root.left), self.height(root.right))
        