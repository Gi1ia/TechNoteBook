class PossiblePath():
    def left_up_right_up(self, m, n):
        """
        move to right, up, down
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for j in range(n):
            for i in range(m):
                if j == 0:
                    dp[i][j] = 1
                    # print
                else:
                    temp = 0
                    for cursor in range(m):
                        temp += dp[cursor][j - 1]

                    dp[i][j] = temp
        
        print(dp)
        return dp[-1][-1]
    
    def count_path(self, m, n):
        """
        move to right, right up, right down
        """
        # ?? Formula == m ** (n - 1)
        dp = [[0 for i in range(n)] for i in range(m + 2)]
        

        dp[m][0] = 1
        
        for j in range(1, n):
            for i in range(1, m + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1]
        
        for row in dp:
            print(row)
        return dp[m][n - 1]
    
    def count_path_followup(self, m, n, points):
        """
        Credit: Yuan 
        Copyright: Yuan
        """
        """
        this.count = new int[m + 2][n];
        this.m = m;
        this.n = n;
        int startX = m;
        int startY = 0;
        int accumulate = 1;
        # TODO: sort points by y axis
        for (int i = 0; i < points.length; i++) {
            accumulate = countPath(startX, startY, accumulate, points[i][0] + 1, points[i][1]);//x + 1 because matrix range of x is [1, m]
            if (accumulate == 0) return 0;
            startX = points[i][0] + 1;
            startY = points[i][1];
        }
        return countPath(startX, startY, accumulate, m, n-1);
        """


obj = PossiblePath()
# print(obj.left_up_right_up(4, 2))
# print(obj.left_up_right_up(5, 2))
# print(obj.left_up_right_up(5, 5))

print(obj.count_path(4, 2))
print(obj.count_path(2, 4))
print(obj.count_path(5, 2))
print(obj.count_path(5, 5))