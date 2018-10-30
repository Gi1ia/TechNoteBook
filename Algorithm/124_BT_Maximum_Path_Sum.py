# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = float('-inf')

    def maxPathSum_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum_down(root)

        return self.sum
    
    def max_sum_down(self, node):
        """ Calculate the max sum from node to its leaves
        """
        if not node:
            return 0
        
        max_left = max(0, self.max_sum_down(node.left))
        max_right = max(0, self.max_sum_down(node.right))
        
        # UPdate global sum
        self.sum = max(self.sum, max_left + max_right + node.val)

        # Return the single path sum
        return max(max_left, max_right) + node.val
