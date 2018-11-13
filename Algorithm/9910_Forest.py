class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Forest():
    def tree_to_forest(self, root, to_delete):
        """
        type root: TreeNode
        type to_delete: List[int]
        return: list[TreeNode]
        """
        if not root:
            return []
        res = []

        
    