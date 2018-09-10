# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            cursor = stack.pop()
            res.append(cursor.val)
            root = cursor.right
        
        return res
            
            
    def inorderTraversal_recursive(self, root):
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
        
        self.private_traversal(root.left, res)
        res.append(root.val)
        self.private_traversal(root.right, res)