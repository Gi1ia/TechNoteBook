class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        '''
        Let the first element of each column to record whether this column should be set zeroes
        Let the first element of each row to record whether this row should be set zeros.
        '''
        column_o = False
        row_o = False
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        row_o = True
                    if j == 0:
                        column_o = True
                    
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        
        
        if row_o:
            for j in range(m):
                matrix[0][j] = 0
        if column_o:
            for i in range(n):
                matrix[i][0] = 0