class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        # self.clear = tuple(bool, bool)

class Solution():
    def sum_tree_set_parent_while_traversal(self, root):
        """ Calculate sum of leave child only
            Defaule parent value is None. 
        """
        if not root:
            return 0
        
        res = 0
        last_visit = None
        current = root
        while current:
            if (not current.left) and (not current.right):
                last_visit = current
                res += current.val
                current = current.parent
            elif current.left and not current.left.parent:
                current.left.parent = current
                current = current.left

            elif current.right and not current.right.parent:
                current.right.parent = current
                current = current.right

            else:
                current = current.parent
        
        return res               

    def sum_tree_seted_parent(self, root):
        """
            Default parent value has been set
        """
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