from heapq import heappush, heappop, heapify
import collections

class SkiScore():
    def ski(self, nodes, edges, start, end):
        """
        nodes: Nodes and corresponding scores {A: 5, B: 7, C: 10}
        edges: Neighbors of each nodes {A: { B:3, C:4 }, B: { D:2, F:1 } }
        """
        visited = set() # If there is no cycle in the graph, no need to use visited
        queue = collections.deque()
        queue.append((start, nodes[start]))

        scores = collections.defaultdict(int)
        scores[start] = nodes[start]
        while queue:
            current = queue.popleft()
            if current[0] in visited:
                continue
            else:
                visited.add(current[0])
            if current[0] == end:
                return current[1]
            if scores[current] > current[1]: # we are looking for largest score
                continue
            for next_node, cost in edges[current[0]].items():
                score = current[1] - cost + nodes[next_node]
                if score > scores[next_node]:
                    queue.append((next_node, score))

        return float('-inf')

    def ski_dijkstra_Bug(self, nodes, edges, start, end):
        #NOTE: Dijkstra can NOT solve this problem
        # Because we are looking for a largest score and it's like a negative weight problem
        # The only way we can make sure to find the 'heaviest' weight route is by BFS/DFS
        # We MUST complete the search.
        # I kept this just because it could be a dijastra example.
        queue = []
        heappush(queue, (-nodes[start], start))

        scores = collections.defaultdict(int)
        scores[start] = nodes[start]

        while queue:
            current_score, current_node = heappop(queue)
            current_score = -current_score
            if current_node == end:
                return current_score

            if scores[current_node] > current_score:
                continue

            for next_node, cost in edges[current_node].items():

                score = current_score - cost + nodes[next_node]
                if score > scores[next_node]:
                    heappush(queue, (-score, next_node))

        return float('-inf')

nodes = {"A":5, "B":7, "C":6, "D":2, "E":4, "F":7, "H":7, "I":3, "J":2}
edges = {"A":{"B":2, "C":3}, "B":{"D":5, "E":6}, "C":{"E":4, "F":4},\
 "D":{"H":7}, "E":{"H":6}, "H":{"I":1, "J":2}, "F":{"J":3}}
start = "A"
end = "J"

# Test 2
nodes2 = {"A":5, "B":10, "C":20, "D":100}
edges2 = {"A":{"B":3}, "B" : {"C":7}, "C":{"D":10, "B":5}}
start2 = "A"
end2 = "D"

obj = SkiScore()
print(obj.ski_dijkstra_Bug(nodes, edges, start, end))
print(obj.ski(nodes2, edges2, start2, end2))

