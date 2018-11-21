"""
Given a room (matrix), 1 means wall, 0 means space,
paint all walls from (0, 0) to (n - 1, n - 1)
"""

import collections

class Solution():
    def paint_wall(self, matrix):
        """
        matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return 0
        # TODO: Valid input (0, 0), (n, n) 
        # What if (n, n) == 1?
                
        height = len(matrix)
        width = len(matrix[0])
        stack = collections.deque()
        stack.append((0, 0))
        path = set()
        path.add((0, 0))
        res = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while stack:
            current = stack.popleft()
            for d in directions:
                x = current[0] + d[0]
                y = current[1] + d[1]
                if x < 0 or y < 0 or x >= height or y >= width \
                    or ((x, y) in path) or matrix[x][y] == 1:
                        res += 1
                        if (x, y) in path:
                            res -= 1
                else:
                    stack.append((x, y))
                    path.add((x, y))
        
        return res - 4

matrix = [[0, 0, 0, 1, 1],[0, 0, 0, 0, 1], [1, 1, 0, 0, 0], [1, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
s = Solution()
print(s.paint_wall(matrix))

