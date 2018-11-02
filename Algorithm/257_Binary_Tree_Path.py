# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        
        res = []
        current =''
        
        self.dfs(root, current, res)
        
        return res
        
    def dfs(self, node, path, res):
        if not node.left and not node.right:
            res.append(path + str(node.val))
            return
        
        if node.left:
            self.dfs(node.left, path + str(node.val) + '->', res)
        
        if node.right:
            self.dfs(node.right, path + str(node.val) + '->', res)
            
            
        