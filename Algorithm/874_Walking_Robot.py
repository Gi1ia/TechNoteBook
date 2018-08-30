class Solution():
    def robot_sim(self, commands, obstacles):
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0

        obstacles_set = set(map(tuple, obstacles))
        res = 0

        for cmd in commands:
            if cmd == -2: # turn left; e.g. first turn will be x--, y = y
                di = (di - 1) % 4
            elif cmd == -1: # turn right: e.g. first turn will be x++, y = y
                di = (di + 1) % 4
            else:
                for k in range(cmd): # Move k units
                    if (x + dx[di], y + dy[di]) not in obstacles_set:
                        x = x + dx[di]
                        y = y + dy[di]
                        res = max(res, x*x + y*y)
        
        return res