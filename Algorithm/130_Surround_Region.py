class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return None
        
        for row in range(len(board)):
            if board[row][0] == 'O':
                self.can_escape(row, 0, board)
            if board[row][len(board[0]) - 1] == 'O':
                self.can_escape(row, len(board[0]) - 1, board)
        
        for column in range(len(board[0])):
            if board[0][column] == 'O':
                self.can_escape(0, column, board)
            if board[len(board) - 1][column] == 'O':
                self.can_escape(len(board) - 1, column, board)
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
        
    
    def can_escape(self, x, y, board):
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != 'O':
            return
        
        board[x][y] = '#'
        self.can_escape(x - 1, y, board)
        self.can_escape(x + 1, y, board)
        self.can_escape(x, y - 1, board)
        self.can_escape(x, y + 1, board)
        
        