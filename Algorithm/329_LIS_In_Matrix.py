import collections

class Solution:
    def longestIncreasingPath_Topological(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        height, width = len(matrix), len(matrix[0])
        step = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # wrap matrix with system.min so we could find out largest value
        new_matrix = [[float("-inf") for _ in range(width + 2)] for _ in range(height + 2)] 
        for i in range(height):
            for j in range(width):
                new_matrix[i + 1][j + 1] = matrix[i][j]

        # initial matrix for outdegree
        outdegree = [[0 for _ in range(width + 2)] for _ in range(height + 2)]
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                for d in directions:
                    if new_matrix[i][j] < new_matrix[i + d[0]][j + d[1]]:
                        outdegree[i][j] += 1

        # looking for largest nodes (node without any indegree)
        leaves = []
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                if outdegree[i][j] == 0:
                    leaves.append((i, j))

        while leaves:
            step += 1
            new_leaves = []
            for node in leaves:
                for d in directions:
                    x, y = node[0] + d[0], node[1] + d[1]
                    # path from large number to small number
                    if new_matrix[x][y] < new_matrix[node[0]][node[1]]:
                        outdegree[x][y] -= 1
                    if outdegree[x][y] == 0:
                        new_leaves.append((x, y))
            
            leaves = new_leaves[:]
        
        return step


    def longestIncreasingPath_DFS(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        height = len(matrix)
        width = len(matrix[0])
        res = 0
        cache = [[0 for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                res = max(self.dfs(matrix, cache, i, j), res)
        
        return res
    
    def dfs(self, matrix, cache, i, j):
        if cache[i][j] != 0:
            return cache[i][j]
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        local_max = 0
        for drct in directions:
            x = i + drct[0]
            y = j + drct[1]
            if x >= 0 and y >= 0 and x < len(matrix) and \
            y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                local_max = max(self.dfs(matrix, cache, x, y), local_path)
        
        cache[i][j] = local_max + 1
        
        return cache[i][j]
