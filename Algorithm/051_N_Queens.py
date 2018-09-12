class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n or n < 1:
            return [[]]

        arrangements = []
        self.dfs([], arrangements, n)

        summary = []
        # draw summary of boards
        for arrangement in arrangements:
            board = []
            for x, y in enumerate(arrangement): # len(arrangement) == n
                temp = "." * n
                location = temp[:y] + 'Q' + temp[y + 1:]
                board.append(location)
            summary.append(baord)
        
        return summary

    def dfs(self, current_rows, res, n):
        """
        :type current_rows: List[int]
            index == row of Q
            key == col of Q
            e.g. [4, 2] means we put two queues already, 
                they are in [0, 4], [1, 2]
        :type res: Result of arrangement
        :return: List[List[int]]
        """
        if len(current_rows) == n: # queue has been put to the last row
            res.append(current_rows[:])
            return
        
        # Trying to put Q in new row
        for col in range(n):
            # row, col, currentResult
            if self.valid(len(current_rows), col, current_rows):
                current_rows.append(col)
                self.dfs(current_rows, res, n)
                current_rows.pop()
        
        return res
        
    def valid(self, x, y, arrangement):
        for row, col in enumerate(arrangement):
            # Valid vertical
            if y == col:
                return False
        
            # Valid diagonal
            if row + col == x + y or row - col == x - y:
                return False
        
        return True
