class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if not m or not n:
            return 0
        
        res = [[0 for x in range(n)] for y in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res[i][j] = 1
                elif i == 0:
                    res[i][j] = res[i][j - 1] 
                elif j == 0:
                    res[i][j] = res[i - 1][j]
                else:
                    res[i][j] = res[i][j - 1] + res[i - 1][j]
        
        return res[m - 1][n - 1]

s = Solution()
print(s.uniquePaths(3, 7))