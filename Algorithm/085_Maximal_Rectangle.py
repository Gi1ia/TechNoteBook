class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        left = [0 for x in range(n)]
        right = [n for x in range(n)]
        height = [0 for x in range(n)]
        res = 0

        for i in range(m):
            current_left = 0
            current_right = n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], current_left)
                else:
                    left[j] = 0
                    current_left = j + 1
            
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], current_left)
                else:
                    right[j] = 0
                    current_right = j
        
            for j in range(n):
                res = max(res, height[j] * (right[j] - left[j]))
            
        
        return res
