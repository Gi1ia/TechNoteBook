class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Build the graph
        self.graph = [[] for _ in range(N)]
        for p1, p2 in dislikes:
            self.graph[p1 - 1].append(p2 - 1)
            self.graph[p2 - 1].append(p1 - 1)
        
        # Save the color
        self.color = [0 for _ in range(N)]
        
        for i in range(N):
            if self.color[i] == 0 and not self.dfs(i, 1):
                return False
        
        return True
        
    
    def dfs(self, v, current):
        self.color[v] = current
        
        for neighbor in self.graph[v]:
            if self.color[neighbor] == current:
                return False
            if self.color[neighbor] == 0 and not self.dfs(neighbor, -current):
                return False
        
        return True