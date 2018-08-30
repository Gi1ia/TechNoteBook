class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        
        res = [[0 for x in range(width)] for y in range(height)]
        
        for i in range(height):
            for j in range(width):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                elif i == 0 and j == 0:
                    res[i][j] = 1
                elif i == 0:
                    res[i][j] = res[i][j - 1]
                elif j == 0:
                    res[i][j] = res[i - 1][j]
                else:
                    res[i][j] = res[i - 1][j] + res[i][j - 1]
                    
        
        return res[height - 1][width - 1]