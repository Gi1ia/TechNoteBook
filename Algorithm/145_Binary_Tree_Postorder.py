# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, res = [], []
        stack.append(root)
        # Reverse every step in preorder traversal
        while stack:
            cursor = stack.pop()
            res.insert(0, cursor.val) 
            if cursor.left:
                stack.append(cursor.left)
            if cursor.right:
                stack.append(cursor.right)
        
        # Another solution is, change sequence while pushing left/right node of preporder,
        # The at last, reverse the entire result list to get the postorder traversal
        return res
        
        
    def postorderTraversal_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, res)
        
        return res
    
    def helper(self, root, res):
        if not root:
            return
        
        if root.left:
            self.helper(root.left, res)
        if root.right:
            self.helper(root.right, res)
        res.append(root.val)
        
        