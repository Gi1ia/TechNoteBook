class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        # self.clear = tuple(bool, bool)

class Solution():
    def sum_tree(self, root):
        if not root:
            return 0
        
        res = 0
        current = root
        while current:
            if current.left:
                temp = current.left
                # Clear left child so we know it has been visited
                current.left = None
                current = temp
            elif current.right:
                temp = current.right
                # Clear right
                current.right = None
                current = temp
            else:
                res += current.val
                current = current.parent
    
        return res