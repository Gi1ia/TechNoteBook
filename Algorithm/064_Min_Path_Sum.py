class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        height = len(grid)
        width = len(grid[0])
        
        res = [[0 for x in range(width)] for y in range(height)]
        
        for i in range(height):
            for j in range(width):
                if i == 0 and j == 0:
                    res[i][j] = grid[i][j]
                elif i == 0:
                    res[i][j] = res[i][j - 1] + grid[i][j]
                elif j == 0:
                    res[i][j] = res[i - 1][j] + grid[i][j]
                else:
                    res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        
        return res[height - 1][width - 1]