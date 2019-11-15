"""Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
"""
class Solution:
    def numTrees(self, n: int) -> int:
        # For BST contains number from 1~n, once the root value is set,
        # the number of nodes on left and right are also being set.
        # This means, we can calculate number of BST with root x, by adding it's unique left subtree and right subtree together.

        # For n == 0, there is only one unique BST
        # For n == 1, there is also only one unique BST

        G = [0] * (n + 1) # this is faster than [0 for _ in range(n + 1)]
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i):
                # For example, if n = 7, and we are calculating number of unique BST of root == 4
                # left subtree will be [1, 2, 3] == G[3],
                # and right subtree will be node [5, 6, 7] which is G[7 - 4] = G[3]
                G[i] = G[j - 1] * G[i - j]
        
        return G[n]



