class Solution:

    def maximalRectangle_dp2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

        Credit: wahcheung
            [
            ["1","0","1","0","0"],
            ["1","0","1","1","1"],
            ["1","1","1","1","1"],
            ["1","0","0","1","0"]
            ]
            策略: 把matrix看成多个直方图, 每一行及其上方的数据都构成一个直方图, 需要考察matrix.size()个直方图
            对于每个点(row, col), 我们最后都计算以这个点上方的连续的'1'往left, right方向延申可以得到的最大的矩形的面积
            通过这种方法获取的矩形一定会把最大的矩形包含在内
            height[row][col]记录的是(row, col)这个坐标为底座的直方图柱子的高度, 如果这个点是'0', 那么高度当然是0了
            left[row][col]记录的是(row, col)这个坐标点对应的height可以延申到的最左边的位置
            right[row][col]记录的是(row, col)这个坐标点对应的height可以延申到的最右边的位置+1
            以上面的matrix为例,
            对于(row=2, col=1)这个点, left=0, right=5, height=1
            对于(row=2, col=2)这个点, left=2, right=3, height=3
            (2,2)这个点与(2,1)紧挨着,left和right却已经变化如此之大了, 这是因为left和right除了受左右两边的'1'影响, 还受到了其上方连续的'1'的制约
            由于点(2,2)上有height=3个'1', 这几个'1'的left的最大值作为当前点的left, 这几个'1'的right的最小值作为当前点的right
            因此, 实际上, 我们是要找以hight对应的这条线段往左右两边移动(只能往全是'1'的地方移动), 可以扫过的最大面积
            当hight与目标最大矩形区域的最短的height重合时, 最大矩形的面积就找到了, 如上面的例子, 就是点(2,3)或(2,4)对应的height
        """
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        left = [0 for x in range(n)]
        right = [n for x in range(n)] # Note: right should initial with n
        height = [0 for x in range(n)]
        
        for i in range(m):
            current_left = 0
            current_right = n
            
            # Height is a row, it store the highest column 1 from left to right (from bottom)
            # If there is a '0', the column is cleared.
            for j in range(n):
                if matrix[i][j] == '0':
                    height[j] = 0
                else:
                    height[j] += 1
            
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(current_left, left[j])
                else:
                    left[j] = 0
                    current_left = j + 1
            
            # From right to left, we store the 'rightest' 1 we can reach with height[j]
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(current_right, right[j])
                else:
                    right[j] = n
                    current_right = j
                
            # We calculate the result at every row.
            for j in range(n):
                res = max(res, height[j] * (right[j] - left[j]))
        
        return res



    def maximalRectangle_dp(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        height = [[0 for x in range(n)] for x in range(m)]
        left = [[0 for x in range(n)] for x in range(m)]
        right = [[n for x in range(n)] for x in range(m)]

        res = 0

        for i in range(m):
            currLeft = 0
            currRight = n
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0:
                        height[i][j] = 1
                        left[i][j] = currLeft
                    else:
                        height[i][j] = height[i - 1][j] + 1
                        left[i][j] = max(left[i - 1][j], currLeft)
                else:
                    height[i][j] = 0
                    left[i][j] = 0
                    currLeft = j + 1

            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    if i == 0:
                        right[i][j] = currRight
                    else:
                        right[i][j] = min(right[i - 1][j], currRight)
                else:
                    right[i][j] = n  # because the height from next row won't reach this row
                    currRight = j

            for j in range(n):
                res = max(res, height[i][j] * (right[i][j] - left[i][j]))

        return res

