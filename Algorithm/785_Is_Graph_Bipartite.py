
class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        
        color = {}
        
        for node, neighbors in enumerate(graph): # iterate every node because there could be single node without any edges
            if node not in color: # Only check those node without been colored
                stack = [(node, neighbors)]
                color[node] = 1
                while stack:
                    current, around = stack.pop()
                    for neighbor in around:
                        if neighbor not in color:
                            color[neighbor] = color[current] ^ 1
                            stack.append((neighbor, graph[neighbor]))
                        elif color[neighbor] == color[current]:
                            return False
            
        return True
                
        