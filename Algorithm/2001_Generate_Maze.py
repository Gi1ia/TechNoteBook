"""
Q: Generate a Maze
Tag: back tracking
"""
class Solution():
    """
    Method 1: Generate path first. Then fill other spot with random blocks.
    Con: This won't guarantee a perfect Maze.
    
    """
    def generate_path(self, grid, start, end):
        """
        """
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
        :used: set(tuple(int, int)); pass by reference
        :rtype: None, if not valid directions
            tuple(int, int), if we have direction left
        """
        directions = ((0, 1), (-1, 0), (0, -1), (1, 0))
        left = directions & used
        if not left:
            return None

        d = left.pop()
        return d


"""
# Defination:
    Perfect: A "perfect" Maze means one without any loops or closed circuits, \
    and without any inaccessible areas. Also called a simply-connected Maze. \
    From each point, there is exactly one path to any other point. \
    The Maze has exactly one solution. In Computer Science terms, \
    such a Maze can be described as a spanning tree over the set of cells or vertices.

    Braid: A "braid" Maze means one without any dead ends. \
    Also called a purely multiply connected Maze. \
    Such a Maze uses passages that coil around and run back into each other \
    (hence the term "braid") and cause you to spend time going in circles \
    instead of bumping into dead ends. \
    A well-designed braid Maze can be much harder than a perfect Maze of the same size.

# Ref:
    [Think Labyrinth](http://www.astrolog.org/labyrnth/algrithm.htm)
    [wikipedia](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
    [A maze lib in github](https://github.com/theJollySin/mazelib)
    [12 way to generate a maze](https://stackoverflow.com/a/23681987)
"""