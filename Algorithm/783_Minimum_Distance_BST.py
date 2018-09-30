"""
Given a Binary Search Tree (BST) with the root node root, 
return the minimum difference between the values of any two different nodes in the tree.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.min_val = float("inf")
        self.prev = float("inf")
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        if not root:
            return self.min_val
        self.inorder(root)
        
        return self.min_val
    
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.min_val = min(self.min_val, abs(node.val - self.prev))
            self.prev = node.val
            self.inorder(node.right)