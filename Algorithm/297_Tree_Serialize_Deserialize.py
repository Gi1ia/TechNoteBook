# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        stack, all_nodes = [], []
        stack.append(root)
        all_nodes.append(str(root.val))
        
        while stack:
            temp = []
            for node in stack:
                if node.left:
                    all_nodes.append(str(node.left.val))
                    temp.append(node.left)
                else:
                    all_nodes.append("null")
                if node.right:
                    all_nodes.append(str(node.right.val))
                    temp.append(node.right)
                else:
                    all_nodes.append("null")
            stack = temp
        
        return ",".join(all_nodes)       

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        
        all_nodes = data.split(",")
        all_nodes = collections.deque(all_nodes)
        current = all_nodes.popleft()
        root = TreeNode(int(current))
        stack = [root]
        
        while stack:
            temp = []
            for node in stack:          
                next_left = all_nodes.popleft() if all_nodes else None
                next_right = all_nodes.popleft() if all_nodes else None
            
                if next_left and next_left != "null":
                    new_left = TreeNode(int(next_left))
                    node.left = new_left
                    temp.append(new_left)
                if next_right and next_right != "null":
                    new_right = TreeNode(int(next_right))
                    node.right = new_right
                    temp.append(new_right)
            stack = temp
        
        return root
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

tree1 = [1,2,3,null,null,4,5]
tree2 = [1,2,2,3,null,null,3,4,null,null,4]