import collections

class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board or not board[0] or len(board[0]) == 1:
            return 0
        
        # Reorder board to straight
        n = len(board)
        straight = []
        index = []
        seq = 1

        for i in reversed(range(n)):
            if seq == 1:
                straight.extend(board[i])
                seq = -1
            else:
                straight.extend(reversed(board[i]))
                seq = 1
                
        # Calculate
        step = 0
        seen = {1:0}      
        possible = collections.deque([1])
        while possible:
            cursor = possible.popleft()
            if cursor == n*n:
                return seen[cursor]
            
            # move to next
            for cursor2 in range(cursor + 1, cursor + 7):
                if cursor2 > n*n:
                    continue
                if straight[cursor2 - 1] != -1:
                    cursor2 = straight[cursor2 - 1]
                if cursor2 not in seen:
                    possible.append(cursor2)
                    seen[cursor2] = seen[cursor] + 1
        
        return -1
        
            
            