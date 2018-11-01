"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        Left point to prev
        right point to after
        """
        if not root:
            return None
        
        head, tail = self.helper(root)
        head.left = tail
        tail.right = head
        return head
    
        
    def helper(self, curr):
        """
        Idea: Construct a DLL for each subtree, then return the head and tail
        """
        head, tail = curr, curr
        if curr.left:
            lhead, ltail = self.helper(curr.left)
            ltail.right = curr
            curr.left = ltail
            head = lhead
        if curr.right:
            rhead, rtail = self.helper(curr.right)
            rhead.left = curr
            curr.right = rhead
            tail = rtail
        return head, tail
        