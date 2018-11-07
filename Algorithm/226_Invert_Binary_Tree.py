# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            current = queue.popleft()
            left = current.left
            right = current.right
            current.left = right
            current.right = left
            if left:
                queue.append(left)
            if right:
                queue.append(right)
        
        return root
        
    
    def invertTree_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root