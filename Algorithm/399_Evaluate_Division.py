import collections

class Solution_UnionFind(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # A:(B, 2.0); string:tuple(string, float)
        self.parents = {}
        
        # Build UF forest
        for i in range(len(equations)):
            v1, v2 = equations[i]
            weight = values[i]
            if v1 not in self.parents and v2 not in self.parents:
                self.parents[v1] = [v2, weight]
                self.parents[v2] = [v2, 1.0]
            elif v1 not in self.parents:
                self.parents[v1] = [v2, weight]
            elif v2 not in self.parents:
                self.parents[v2] = [v1, 1/weight]
            else: # Union them
                p1 = self.find(v1)
                p2 = self.find(v2)
                
                # NOTE: compare only the parent not the weight
                if p1[0] != p2[0]:
                    # self.parents.pop(v1, None)
                    self.parents[v1] = [p2[0], weight * p2[1] * p1[1]]
        
        res = []
        for query in queries:
            x, y = query
            if x not in self.parents or y not in self.parents:
                res.append(-1.0)
                continue
            
            xp = self.find(x) # x, x/xp
            yp = self.find(y) # y, y/yp
            
            # NOTE: compare only the parent not the weight
            if xp[0] != yp[0]:
                res.append(-1.0)
            else:
                res.append(xp[1]/yp[1])
        
        return res
            
    
    def find(self, x):
        if x != self.parents[x][0]:
            root = self.find(self.parents[x][0])
            self.parents[x][1] *= root[1]
            self.parents[x][0] = root[0]
        
        return self.parents[x]


class Solution_BFS:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # NOTE: Zero?
        # NOTE: Not in dictionary?
        graph = collections.defaultdict(list)
        
        for i in range(len(equations)):
            v1, v2 = equations[i]
            w1, w2 = values[i], 1/values[i]
            graph[v1].append((v2, w1))
            graph[v2].append((v1, w2))
        
        res = []
        for q1, q2 in queries:
            if (not q1 in graph) or (not q2 in graph):
                res.append(float(-1))
                # NOTE: if we can't find the node, continue
                continue
                
            val = self.bfs(graph, q1, q2)
            res.append(val)
       
        return res

    
    def bfs(self, graph, q1, q2):
        queue = collections.deque()
        queue.append((q1, 1.0))
        seen = set()
        while queue:
            current, val = queue.popleft()
            seen.add(current)
            if current == q2:
                return val

            neibors = graph[current]
            for n in neibors:
                if n[0] not in seen:
                    seen.add(n[0])
                    queue.append((n[0], val * n[1]))
        
        return float(-1)
                
                
                