# Uber
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right 


    def kthSmallest_recursive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self._helper(root)
        return self.res
    
    def _helper(self, node):
        if not node:
            return 
        self._helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self._helper(node.right)