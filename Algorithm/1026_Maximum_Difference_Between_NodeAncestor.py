"""Given the root of a binary tree, 
find the maximum value V for which there exists different nodes A and B where 
V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, 
or any child of A is an ancestor of B.)

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        """ Solution I
        Solution with Stack has much better performance.
        Using stack to maintain max and min through the way
        """
        res = 0
        stack = [[root, root.val, root.val]] # node, max, min
        
        while stack:
            temp, cur_mx, cur_mn = stack.pop()
            if temp.val > cur_mx:
                cur_mx = temp.val
            if temp.val < cur_mn:
                cur_mn = temp.val
            if cur_mx - cur_mn > res:
                res = cur_mx - cur_mn
                
            if temp.left:
                stack.append([temp.left, cur_mx, cur_mn])
            if temp.right:
                stack.append([temp.right, cur_mx, cur_mn])
        
        return res
            
    def maxAncestorDiff_dfs(self, root: TreeNode) -> int:
        """Solution II
        DFS solution is more clean and straight forward.
        """
        return self.dfs(root, root.val, root.val)
        
    def dfs(self, root, min_val, max_val):
        if not root:
            return max_val - min_val

        max_val = max(max_val, root.val)
        min_val = min(min_val, root.val)
        return max(self.dfs(root.left, min_val, max_val), self.dfs(root.right, min_val, max_val))
            
        