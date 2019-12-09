class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m = len(s)
        n = len(p)

        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True # compare between None and None

        # Edge case: if s == "", p is all '*'
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {'?', s[i - 1]}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = False

        # print. Can be removed
        print(" ", " ",  list(p))
        for i in range(m + 1):
            if i == 0:
                dp[i].insert(0, " ")
            else:
                dp[i].insert(0, s[i - 1])
            print(dp[i])
        
        return dp[-1][-1]

obj = Solution()
print(obj.isMatch('bbaac', '*a*a*'))
# print(obj.isMatch("", "?**"))
# print(obj.isMatch("", "*****"))