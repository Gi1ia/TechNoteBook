from collections import defaultdict

class CurrencyLookUP():
    def __init__(self, currency, values):
        self.graph = defaultdict(defaultdict)
        
        for i in range(len(currency)):
            c1, c2 = currency[i]
            w1, w2 = values[i], 1/values[i]
            self.graph[c1][c2] = w1
            self.graph[c2][c1] = w2
        
        self.N = len(self.graph)      
        self.parents = {}
        self.size = {}
        for key, val in self.graph.items():
            self.parents[key] = (key, 1.0)
            self.size[key] = 1

    def find(self, x):
        parent = self.parents[x]
        while parents[x][0] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        size1 = self.size[x1]
        size2 = self.size(x2)
        
        if size1 > size2:
            val1 = p1[1]
            val2 = self.graph[p2][p1]
            self.parents[x2] = (p1[0], val1 * val2)
            self.size[x1] += self.size[x2]
        else:
            val2 = p2[1]
            val1 = self.graph[p1][p2]
            self.parents[x1] = (p2[0], val1 * val2)
            self.size[x2] += self.size[x1]
        