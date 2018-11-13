# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Left, root, right
    # TODO: Morris Traversal

    def inorderTraversal2(self, root):
        if not root:
            return []
        stack, res = [], []
        current = root
        
        while stack or current:
            # Push all left node into stack first
            while current:
                stack.append(current)
                current = current.left
            
            # Here, since we push the left node from root,
            # so before we push current.right, 
            # the root has been visited
            current = stack.pop()
            res.append(current.val)
            stack.append(current.right)
        
        return res

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