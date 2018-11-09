class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if not edges:
            return []
        
        size = len(edges)
        seen = UnionFind(size)
        
        for edge in edges:
            # edge[0], edge[1] are two v of the edge
            if not seen.union(edge[0], edge[1]):
                return edge
                
        return []

class UnionFind():
    def __init__(self, k):
        self.parents = [i for i in range(k + 1)] # num of v == num of e + 1
        # rank ~ size
        self.size = [1 for i in range(k + 1)]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False # do not (need) union
        
        if self.size[px] > self.size[py]:
            self.parents[py] = px
            self.size[py] += self.size[px]
        else: # self.size[px] <= self.size[py]:
            self.parents[px] = py
            self.size[px] += self.size[py]
            
        return True # unioned