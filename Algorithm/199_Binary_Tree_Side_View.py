# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        res = []
        stack = [root]
        while stack:
            next_level = []
            for node in stack:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(stack[-1].val)
            stack = next_level
        
        return res
        
        
        