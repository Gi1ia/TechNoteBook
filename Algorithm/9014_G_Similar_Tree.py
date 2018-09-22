# G
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def is_similar(self, root1, root2):
        """
        time complexity: ?
        Is it able to be improved?
        """
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False

        if root1.val != root2.val:
            return False
        
        left = self.is_similar(root1.left, root2.left) and\
            self.is_similar(root1.right, root2.right)
        right = self.is_similar(root1.right, root2.left) and\
            self.is_similar(root1.left, root2.right)
        if left or right:
            return True
        
        return False
