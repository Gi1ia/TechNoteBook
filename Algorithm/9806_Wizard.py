from collections import deque, defaultdict
from heapq import heappush, heappop, heapify

class Wizard():
    def __init__(slef):
        self.dst = 9
    
    def shortest_single_dict(self, wizards):
        """
        wizards: List[List[int]]
        Use single dictionary to implement dijkstra. It works, but will waste some space.
        """
        visited = set()
        check = []
        heappush(check, (0, 0, wizards[0])) # distance, wizard_id, wizard_neighbors

        distance = {}
        distance[0] = 0
        for i in range(1, 10):
            distance[i] = float('inf')

        while check:
            dis, current, neighbors = heappop(check)
            if current in visited:
                continue
            else:
                visited.add(current)

            print(check)
            print(distance)
            # find the 10th wizard
            if current == self.dst:
                return distance[current]

            curr_dis = distance[current]
            for neighbor in neighbors:
                e = (neighbor - current) ** 2
                if curr_dis + e < distance[neighbor]:
                    distance[neighbor] = curr_dis + e
                heappush(check, (distance[neighbor], neighbor, wizards[neighbor]))
        
        return float('inf')

    def cheapest_two_dict_dijkstra(self, wizards):
        if not wizards: return 0
        #n = len(wizards)
        source, dest = 0, 9
        n = 10
        cost = [float('inf')] * n
        cost[source] = 0
        cur_costs = { source : 0 }
        for _ in range(n):
            if not cur_costs: break
            next_costs = dict()
            for u, cost_u in cur_costs.iteritems():
                for v in wizards[u]:
                    cost_v = cost_u + (v - u) ** 2
                    cost[v] = min(cost[v], cost_v)
                    next_costs[v] = min(next_costs.get(v, float('inf')), cost[v])
            cur_costs = next_costs
        return cost[dest]

obj = Wizard()
wizards = [[1, 2], [3], [3, 4], [4], [5, 6, 7], [8], [7], [8, 9], [9], [9]]
wizards2 = [[1, 5, 9], [2, 3, 9], [4], [], [], [9], [], [], [], []]
wizards3 = [[1, 3, 4], [2, 3, 1], [4], [], [9], [8], [9], [], [9], []]
print(obj.shortest(wizards3))

        
        
        
