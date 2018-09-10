# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [], []
        stack.append(root)
        
        while stack:
            cursor = stack.pop()
            res.append(cursor.val)
            # We need to push right node fisrt, in order to pop left node to get the value.
            if cursor.right:
                stack.append(cursor.right)
            if cursor.left:
                stack.append(cursor.left)
        
        return res
        
    def preorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.private_traversal(root, res)
        
        return res
        
    def private_traversal(self, root, res):
        if not root:
            return
        
        res.append(root.val)
        if root.left:
            self.private_traversal(root.left, res)
        if root.right:
            self.private_traversal(root.right, res)