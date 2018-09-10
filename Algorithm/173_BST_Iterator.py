# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        :Analysis:
            next() => O(h); in fact average O(1) time??
            hasNext() => O(1)
            Space => O(h)
        """
        self.stack = []
        self.pushAll(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack
        

    def next(self):
        """
        :rtype: int
        """
        current = self.stack.pop()
        self.pushAll(current.right)
        return current.val
        
    def pushAll(self, node):
        # make sure we don't push None node into stack
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())