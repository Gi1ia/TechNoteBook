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
        res = self.recursive(root, to_delete, [])

        return res

    def recursive(self, node, to_delete, res):
        if not node:
            return []
        
        if node in to_delete:
            if node.left and node.left not in to_delete:
                res.append(node.left)
            if node.right and node.right not in to_delete:
                res.append(node.right)
        
        l = self.recursive(node.left, to_delete, [])
        r = self.recursive(node.right, to_delete, [])
        
        res.extend(l)
        res.extend(r)

        return res

    