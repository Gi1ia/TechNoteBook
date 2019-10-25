# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        stack = [(root, sum - root.val, [root.val])]
        res = []
        
        while stack:
            current, val, path = stack.pop()
            if not current.left and not current.right and val == 0:
                res.append(path)
            if current.left:
                stack.append((current.left, val - current.left.val, path + [current.left.val]))
            if current.right:
                stack.append((current.right, val - current.right.val, path + [current.right.val]))
        
        return res

        