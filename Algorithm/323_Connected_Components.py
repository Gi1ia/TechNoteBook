class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[x] > rank[y]:
                    # NOTE: here we need to point the parent node's parent to the new parent
                    parents[py] = px
                    rank[x] += 1
                else:
                    parents[px] = py
                    rank[y] += 1
        
        parents = [i for i in range(n)]
        rank = [0] * n
        for p1, p2 in edges:
            union(p1, p2)
        
        
        clusters = set()
        for i in range(n):
            clusters.add(find(i))
        
        return len(clusters)