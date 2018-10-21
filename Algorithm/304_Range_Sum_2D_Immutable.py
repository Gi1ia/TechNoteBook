class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return
        height, width = len(matrix), len(matrix[0])
        
        # cumulative sum matrix
        self.storage = [[0 for _ in range(width + 1)] for _ in range(height + 1)]       
        for i in range(1, height + 1):
            for j in range(1, width + 1):
                self.storage[i][j] = self.storage[i - 1][j] + self.storage[i][j - 1] + \
                    matrix[i - 1][j - 1] - self.storage[i - 1][j - 1]
        
        self.matrix = matrix
      

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        region = self.storage[row2 + 1][col2 + 1] - \
            self.storage[row2 + 1][col1] - self.storage[row1][col2 + 1] + self.storage[row1][col1]
        
        return region


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)