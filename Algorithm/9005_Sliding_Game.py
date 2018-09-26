"""

"""
import collections
def sliding_game(board, x, y):
    """
    moving (x, y) to (board[-1][-1])
    """
    # TODO: valid

    q = collections.deque()
    height = len(board)
    width = len(board[0])
    q.append((height - 1, width - 1))
    seen = {}
    seen[(height - 1, width - 1)] = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    while q:
        current = q.pop()
        for d in directions:
            next_x = current[0] + d[0]
            next_y = current[1] + d[1]
            if next_x == x and next_y == y:
                return seen[current] + 1
            if (next_x, next_y) not in directions and next_x >= 0 \
            and next_y >= 0 and next_x < height and next_y < width:
                seen[(next_x, next_y)] = seen[current] + 1
                q.append((next_x, next_y))
    
    