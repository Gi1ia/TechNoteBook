class PossiblePath():
    def left_up_right_up(self, m, n):
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

# ?? Formula == m ** (n - 1)
obj = PossiblePath()
print(obj.left_up_right_up(2, 2))
print(obj.left_up_right_up(5, 2))
print(obj.left_up_right_up(5, 5))