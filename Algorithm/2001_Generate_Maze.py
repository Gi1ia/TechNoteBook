class Solution():
    def generate_path(self, grid, start, end):
        if not grid or not grid[0]:
            return []
        
        path.append(start)
        visited.add(start)
        res = self.dfs(grid, end, path, visited)
        return res
    
    def dfs(self, grid, end, path, visited):
        prev = path[-1]
        if prev[0] == end[0] and prev[1] == end[1]:
            return path

        # Get a random direction    
        used = set()
        d = self.get_random(used)
        x, y = prev[0] + d[0], prev[1] + d[1]

        while x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or ((x, y) in visited):
            d = self.get_random(used)
            if not d:
                return
            x, y = prev[0] + d[0], prev[1] + d[1]

        visited.add((x, y))
        path.append((x, y))
        self.dfs(grid, end, path, visited)
        path.pop()
        # TODO: find a way to record dead end?
        # This is not efficient.
        visited.discard((x, y)) 

    def get_random(self, used):
        """
        :rtype: None, if not valid directions
            tuple(int, int), if we have direction left
        """
        directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
        left = directions & used
        if not left:
            return None

        r = random.randint(0, len(left))
        d = left[r]
        used.add(d)
        return d


