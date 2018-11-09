import collections

class UnionFind():
    def __init__(self, n):
        self.parent = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
        for i in range(n):
            self.parent[i] = i
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
        # Another way to find parent
        # while x != parent[x]:
        #     parent[x] = parent[parent[x]]
        #     x = parent[x]
        # return x
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return
        
        if self.size[parent_x] > self.size[parent_y]:
            self.parent[parent_y] = parent_x
            self.size[parent_y] += self.size[parent_x]
        else:
            self.parent[parent_x] = parent_y
            self.size[parent_x] += self.size[parent_y]

class Islands_UnionFind():
    def num_islands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        # In order to use union find, 
        # we need to convert the 2d data to 1d
        # grid[i][j] = new_grid[i * row + j]
        height = len(grid)
        width = len(grid[0])
        union_find = UnionFind(height * width)

        for i in range(height):
            for j in range(width):
                if grid[i][j] != "1":
                    continue
                if j + 1 < width and grid[i][j + 1] == "1":
                    union_find.union(i * width + j, i * width + j + 1)
                if i + 1 < height and grid[i + 1][j] == "1":
                    union_find.union(i * width + j, (i + 1) * width + j)
                if i - 1 >= 0 and grid[i - 1][j] == "1":
                    union_find.union(i * width + j, (i - 1) * width + j)
                if j - 1 >= 0 and grid[i][j - 1] == "1":
                    union_find.union(i * width + j, i * width + j - 1)
        
        seen_island = [0 for _ in range(height * width)]
        res = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == "1":
                    x = union_find.find(i * width + j)
                    if seen_island[x] == 0:
                        res += 1
                        seen_island[x] += 1
                    else:
                        seen_island[x] += 1
        
        return res


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