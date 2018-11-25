class Solution:
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        if not stones:
            return 0
        
        N = len(stones)
        
        self.parents = [i for i in range(N)]
        self.size = [1 for i in range(N)]
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                x1, y1 = stones[i]
                x2, y2 = stones[j]
                if x1 == x2 or y1 == y2:
                    self.union(i, j)
        
        # print(self.parents)
        # print(self.size)
        
        cluster = set()
        for i in range(N):
            pi = self.find(i)
            cluster.add(pi)
        
        return N - len(cluster)
        

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        
        if px == py:
            return
        
        if self.size[x] > self.size[y]:
            self.parents[py] = px
            self.size[py] += self.size[px]
        else:
            self.parents[px] = py
            self.size[px] += self.size[py]
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]