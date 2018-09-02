import collections

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        # TODO: validate input
        height = len(maze)
        width = len(maze[0])

        visited = [[False for x in range(width)] for y in range(height)]
        queue = collections.deque()
        queue.append(start)

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # Mark start point as visited
        visited[start[0]][start[1]] = True

        while queue:
            current = queue.popleft()
            current_x, current_y = current[0], current[1]
            if current_x == destination[0] and current_y == destination[1]:
                return True

            for drct in directions:
                x = current_x + drct[0]
                y = current_y + drct[1]
                # Keep moving until we hit the illegal boundary
                while (x >=0 and y >= 0 and x < height and y < width and maze[x][y] == 0):
                    x += drct[0]
                    y += drct[1]
                # Move back to legal point
                x -= drct[0]
                y -= drct[1]
                # Check if the point is visited or not to eliminate dead loop.
                if visited[x][y] is False:
                    queue.append([x, y])
                    visited[x][y] = True

        return False

maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start = [0, 4]
end = [4, 4]

s = Solution()
print(s.hasPath(maze, start, end))