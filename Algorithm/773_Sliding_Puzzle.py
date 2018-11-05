import unittest

class Solution:
    def eight_puzzle(self, board):
        if not board or not board[0]:
            return 0

        start_str = "".join(str(i) for row in board for i in row)
        moves = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4, 6], \
        4:[1, 3, 5, 7], 5:[2, 4, 8], 6:[3, 7], 7:[4, 6, 8], 8:[5, 7]}
        visited, step = set(), 0
        current_list, next_list = [start_str], []

        while current_list:
            for current in current_list:
                if current == '123456780':
                    return step
            
                cursor = current.index('0') # get index of '0' tile
                for next_cursor in moves[cursor]:
                    arr = [c for c in current]
                    arr[next_cursor], arr[cursor] = arr[cursor], arr[next_cursor]
                    next_str = "".join(arr)
                    if next_str not in visited:
                        next_list.append(next_str)
                        visited.add(next_str)
            current_list = next_list
            next_list = []
            step += 1
        
        return -1


    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0

        start_str = "".join(str(i) for row in board for i in row)
        moves = {0:[1, 3], 1:[0, 2, 4], 2:[1, 5], 3:[0, 4], \
        4:[1, 3, 5], 5:[2, 4]}

        visited, step = set(), 0
        current_list, next_list = [start_str], []

        while current_list:
            for current in current_list:
                if current == "123450":
                    return step
                
                cursor = current.index('0') # we can move tiles around 0 each time
                for next_cursor in moves[cursor]:
                    arr = [c for c in current]
                    arr[next_cursor], arr[cursor] = arr[cursor], arr[next_cursor]
                    next_str = "".join(arr)
                    if next_str not in visited:
                        next_list.append(next_str)
                        visited.add(next_str)
            current_list, next_list = next_list, []
            step += 1
        
        return -1

solver = Solution()
origin = "413578602"
origin2 = "521760834"
print(solver.eight_puzzle(origin2))

