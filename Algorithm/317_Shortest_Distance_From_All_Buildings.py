class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if not grid or not grid[0]:
            return -1
        
        m = len(grid)
        n = len(grid[0])

        
