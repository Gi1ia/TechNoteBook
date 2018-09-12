# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#FB #eBay #G #HashTable

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack, res = [], []
        column = {}
        stack.append((root, 0))
        while stack:
            next_stack = []
            for node, col in stack:
                column.setdefault(col, []).append(node.val)
                if node.left:
                    next_stack.append((node.left, col - 1))
                if node.right:
                    next_stack.append((node.right, col + 1))
            stack = next_stack
        
        vertical_keys = sorted(column.keys())
        for k in vertical_keys:
            res.append(column[k])
        
        return res
        
        