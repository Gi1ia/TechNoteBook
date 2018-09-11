# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 102 is almost the same
# 314 could be follow up
class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack, res = [], []
        stack.append(root)
        level = 0
        while stack:
            row, next_stack = [], []
            for node in stack:
                row.append(node.val)
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            res.insert(0, row)
            level += 1
            stack = next_stack
        
        return res
    
    
    def levelOrderBottom_reverse_102(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        stack, res = [], []
        stack.append(root)
        while stack:
            level, temp = [], [] 
            for node in stack:
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(level)
            stack = temp
        
        return res[::-1]