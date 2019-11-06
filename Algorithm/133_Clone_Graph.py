"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        mapping = {}
        copyNode = Node(node.val, [])
        mapping[node] = copyNode
        
        queue = collections.deque()
        queue.append(node)
        
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in mapping:
                    newNode = Node(neighbor.val, [])
                    mapping[neighbor] = newNode
                    mapping[current].neighbors.append(newNode)
                    queue.append(neighbor)
                else:
                    newNeighbor = mapping[neighbor]
                    mapping[current].neighbors.append(newNeighbor)
        
        return copyNode