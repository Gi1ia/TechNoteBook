class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        
        return False
        
    
    def dfs(self, board, word, x, y, cursor):
        if cursor == len(word):
            return True
        
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False
        
        if board[x][y] != word[cursor]:
            return False
        
        temp = board[x][y]
        board[x][y] = '#'
        
        res = self.dfs(board, word, x - 1, y, cursor + 1) or \
        self.dfs(board, word, x + 1, y, cursor + 1) or \
        self.dfs(board, word, x, y - 1, cursor + 1) or \
        self.dfs(board, word, x, y + 1, cursor + 1)
        
        board[x][y] = temp
        
        return res

s = Solution()
test_case = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

test_case2 = [["C","A","A"],["A","A","A"],["B","C","D"]]

word2 = "AAB"

print(s.exist(test_case2, word2))