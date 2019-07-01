# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.travel(root, res, 0)
        
        return res
        
    def travel(self, current, res, level):
        if not current:
            return
        
        if len(res) <= level:
            new_level = collections.deque()
            res.append(new_level)
        
        temp = res[level]
        if level % 2 == 0:
            temp.append(current.val)
        else:
            temp.appendleft(current.val)
            
        self.travel(current.left, res, level + 1)
        self.travel(current.right, res, level + 1)
        
    
    def zigzagLevelOrder_BFS(self, root: TreeNode) -> List[List[int]]:
        """
        BFS, append leverl to the result. 
        O(n); 63%; 40 ms;13.4 MB
        """
        if not root:
            return []
        
        stack = collections.deque()
        stack.append(root)
        temp = []
        res = []
        flag = 1
        
        while stack:
            for i in range(len(stack)):
                node = stack.popleft()
                temp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            
            res.append(temp[::flag])
            temp = []
            flag *= -1
        
        return res