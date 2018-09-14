# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        if key < root.val:
            self.deleteNode(root.left, key)
        elif key > root.val:
            self.deleteNode(root.right, key)
        else: # find the node to delete
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            # if the node have both left and right children,  \
            # we replace its value with the minmimum value in the right subtree \
            # and then delete that minimum node in the right subtree
                replace = self.find_right_minimum(root.right)
                root.val = replace.val
                # delete the minimum node (note the value is not key anymore) in right subtree
                root.right = self.deleteNode(root.right, root.val)

        return root
     
    def find_right_minimum(self, node):
        while node.left != None:
            node = node.left
        return node

    def deleteNode_wrong(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        
        current = root
        while current and current.val != key:
            if key > current.val:
                current = current.right
            elif key < current.val:
                current = current.left
        
        if not current: # Node to delete is not in the tree
            return root
        
        if not current.left and not current.right:
            return None # Bug here; Unable to handle delete the node itself.
        elif current.left and not current.right:
            current.val = current.left.val
            current.left = current.left.left
            current.right = current.left.right
        elif current.right and not current.left:
            current.val = current.right.val
            current.left = current.right.left
            current.right = current.right.right
        else:
            replace = self.find_right_minimum(current.right)
            current.val = replace.val
            current.right = self.deleteNode_wrong(current.right, current.val)

        return root

root1 = [5,3,6,2,4,None,7]
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(None)
root.right.right = TreeNode(7)
key =3
s = Solution()
root2 = s.deleteNode(root, key)

