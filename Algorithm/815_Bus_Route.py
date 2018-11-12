class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if not routes:
            return -1
        if S == T:
            return 0
        
        routes = [set(r) for r in routes]
        
        # on bus, what buses we can take from it
        graph = collections.defaultdict(set)
        
        for i, route1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                route2 = routes[j]
                for r in route2:
                    if r in route1:
                        graph[i].add(j)
                        graph[j].add(i)
        
        took, targets = set(), set()
        queue = collections.deque()
        for node, route in enumerate(routes):
            if S in route:
                took.add(node)
                queue.append((node, 1))
            if T in route:
                targets.add(node)
        
        # start or end stop is not in our routes
        if not took or not targets:
            return -1
        
        while queue:
            bus, depth = queue.popleft()
            if bus in targets:
                return depth
            for next_bus in graph[bus]:
                if next_bus not in took:
                    took.add(next_bus)
                    queue.append((next_bus, depth + 1))
        
        return -1
            
        
        
            
        
       