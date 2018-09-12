# Exactly the same of #51, return sum instead

class Solution:
    def __init__(self):
        self.sum = 0
         
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n < 1:
            return 0
        
        self.dfs([], n)
        
        return self.sum
        
    def dfs(self, current_arrangement, n):
        if len(current_arrangement) == n:
            self.sum += 1
            return
        
        for col in range(n):
            if self.valid(len(current_arrangement), col, current_arrangement):
                current_arrangement.append(col)
                self.dfs(current_arrangement, n)
                current_arrangement.pop()
        return
    
    def valid(self, x, y, arrangement):
        for row, col in enumerate(arrangement):
            if y == col:
                return False
            if x + y == row + col or x - y == row - col:
                return False
        return True