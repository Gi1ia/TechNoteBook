# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []
        self._distance(root, target, K, res)
        
        return res
    
    def _distance(self, root, target, K, res):
        """
        return distance from root to target
        return -1 if target does not found from root
        """
        if not root:
            return -1
        
        if root == target:
            self.collect(target, K, res)
            return 0
        
        l = self._distance(root.left, target, K, res)
        r = self._distance(root.right, target, K, res)
        
        # Target in left subtree
        # Target to root.left == l -> target to root == l + 1
        # -> Target to root.right == l + 2
        if l >= 0:
            if l + 1 == K: # root has k distance to target 
                res.append(root.val)
            else:
                self.collect(root.right, K - (l + 2), res)
            return l + 1
        
        # Target in right subtree
        if r >= 0:
            if r + 1 == K:
                res.append(root.val)
            else:
                self.collect(root.left, K - (r + 2), res)
            return r + 1
        
        return -1
    
    def collect(self, root, distance, res):
        """
        collect nodes below root
        """
        if not root or distance < 0:
            return
        if distance == 0:
            res.append(root.val)
            
        self.collect(root.left, distance - 1, res)
        self.collect(root.right, distance - 1, res)
            
        
    