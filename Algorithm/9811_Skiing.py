class SkiScore():
    def ski(self, nodes, edges, start, end):
        """
        nodes: Nodes and corresponding scores {A: 5, B: 7, C: 10}
        edges: Neighbors of each nodes {A: { B:3, C:4 }, B: { D:2, F:1 } }
        """
        visited = set()
        visited.add(start)
        queue = collections.deque()
        queue.append((start, nodes[start]))

        scores = collections.defaultdict(int)
        scores[start] = nodes[start]
        while queue:
            current = queue.popleft()
            if current[0] == end:
                return current[1]
            if scores[current] > current[1]: # we are looking for largest score
                continue
            for next_node, cost in edges[current].items():
                score = current[1] - cost + nodes[next_node]
                if score > scores[next_node]:
                    queue.append((next_node, score))

        return float('-inf')

