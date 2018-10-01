class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Case 1: One node has two parents
        # Case 2: Graph has a loop
        # Case 3: Graph has a loop and one node has two parents