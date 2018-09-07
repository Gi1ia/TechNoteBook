"""
Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle. Note that only the corners need to have the value 1. Also, all four 1s used must be distinct.

Example 1:
Input: grid = 
[[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
Output: 1
Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
 

Example 2:
Input: grid = 
[[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]]
Output: 9
Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
 

Example 3:
Input: grid = 
[[1, 1, 1, 1]]
Output: 0
Explanation: Rectangles must have four distinct corners.
 

Note:
The number of rows and columns of grid will each be in the range [1, 200].
Each grid[i][j] will be either 0 or 1.
The number of 1s in the grid will be at most 6000.
"""
import collections

class Solution:
    def countCornerRectangles_CountConers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = collections.Counter()

        res = 0
        for row in grid:
            for x, x_value in enumerate(row):
                if x_value == 1:
                    for y, y_value in enumerate(row[x + 1:]):
                        if y_value == 1:
                            res += count[x, y] # this will (x, y) as tuple
                            # res += count[(x, y)] # Also works
                            count[x, y] += 1
        
        return res

    def countCornerRectangles_BruteForce_TLE(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        # Can't form rectangles with one row
        if len(grid) == 1:
            return 0
            
        pair = [set() for _ in range(len(grid))]
        # Create pair set in row[i]
        for i in range(len(grid)):
            for x, x_value in enumerate(grid[i][:-1]):
                for y, y_value in enumerate(grid[i][x + 1:]):
                    if x_value == 1 and y_value == 1:
                        pair[i].add((x, y))
        
        res = 0
        for i in range(1, len(pair)):
            for j in range(0, i):
                res += len(pair[i] & pair[j])
        
        return res

grid = [[1, 0, 0, 1, 0],\
[0, 0, 1, 0, 1],\
[0, 0, 0, 1, 0],\
[1, 0, 1, 0, 1]]
grid2 = [[1, 1, 1],\
[1, 1, 1],\
[1, 1, 1]]
s = Solution()
print(s.countCornerRectangles_CountConers(grid2))

