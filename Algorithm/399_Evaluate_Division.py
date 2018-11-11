class Solution:
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
                
                
                