"""
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
import collections

class Solution:
    def wallsAndGates_BFS(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return 
        
        queue = collections.deque([])
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append((i + 1, j, 1))
                    queue.append((i - 1, j, 1))
                    queue.append((i, j + 1, 1))
                    queue.append((i, j - 1, 1))
                    while queue:
                        x, y, distance = queue.popleft()
                        if x < 0 or y < 0 or x >= len(rooms)\
                        or y >= len(rooms[0]) or rooms[x][y] < distance:
                            continue
                        rooms[x][y] = distance
                        queue.extend([(x + 1, y, distance + 1), (x - 1, y, distance + 1), (x, y - 1, distance + 1), (x, y + 1, distance + 1)])
                            
    
    def walls_and_gates_DFS(self, rooms):
        if not rooms or not rooms[0]:
            return 
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.fill_distance(rooms, i, j, 0)
        
    def fill_distance(self, rooms, x, y, distance):
        if x < 0 or y < 0 or x >= len(rooms) or y >= len(rooms[0]) or distance > rooms[x][y]:
            return
        
        rooms[x][y] = distance
        self.fill_distance(rooms, x - 1, y, distance + 1)
        self.fill_distance(rooms, x + 1, y, distance + 1)
        self.fill_distance(rooms, x, y - 1, distance + 1)
        self.fill_distance(rooms, x, y + 1, distance + 1)
