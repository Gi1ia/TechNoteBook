"""
    Give a matrix, find a smallest square that their sum large then target K
"""
class Matrix_Sum():
    def smallest_square(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :return: List[List[int]]; stands for two points
        """
        if not matrix or not matrix[0]:
            return [[0, 0], [0, 0]]
        
        height, width = len(matrix), len(matrix[0])
        N = min(height, width)
        rectangle_sum = [[0 for _ in range(width + 1)] for _ in range(height + 1)]

        # cumulative sum
        for i in range(height):
            for j in range(width):
                rectangle_sum[i + 1][j + 1] = rectangle_sum[i][j + 1] + \
                    rectangle_sum[i + 1][j] - rectangle_sum[i][j] + matrix[i][j]
        
        for step in range(1, N + 1): # square side length
            for i in range(step, height + 1):
                for j in range(step, width + 1):
                    current = rectangle_sum[i][j] - rectangle_sum[i - step][j] - rectangle_sum[i][j - step]\
                        + rectangle_sum[i - step][j - step]
                    if current >= target:
                        return [[i - step, j - step], [i - 1, j - 1]]
        
        return [[0, 0], [0, 0]]


matrix = [\
[3, 0, 1, -4, 2],\
[-5, -3, 3, 2, 1],\
[1, 2, 0, 1, -5],\
[-4, 1, 0, 1, -7],\
[1, 0, 3, 0, -5]]
s = Matrix_Sum()
ans = s.smallest_square(matrix, 6)
print(ans)
