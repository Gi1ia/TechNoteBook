# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        # build queue
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()

            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level + 1)) # append tuple only. Do not include list
                    queue.append((node.right, level + 1))