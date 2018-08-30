import collections

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j)
        
        return count
        
        
    def dfs(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1":
            return
        
        grid[x][y] = "#"
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)

    def numIslands_BFS(self, grid):
        
        queue = collections.deque()
        count = 0

        for i in range(len(grid)):
        	for j in range(len(grid[0])):
        		if grid[i][j] == "1":
        			count += 1
        			grid[i][j] = "#"
        			queue.extend([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])
        			while queue:
        				x, y = queue.popleft()
        				if x < 0 or y < 0 or x >= len(grid) or \
        				y >= len(grid[0]) or grid[x][y] != "1":
        					continue
        				grid[x][y] = "#"
        				queue.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

        return count