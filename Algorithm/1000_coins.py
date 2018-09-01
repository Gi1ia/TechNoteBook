"""
# MiniMax

There are n coins in a line. (Assume n is even).
Two players take turns to take a coin from one of the ends of the line until there are no more coins left.
The player with the larger amount of money wins.

1. Would you rather go first or second? Does it matter?
2. Assume that you go first, describe an algorithm to compute the maximum amount of money you can win.
"""
class Solution():
    def coins_in_lines(self, coins):
        """
        : How many coins can the first player get?
        : coins: list[int]
        """
        l = len(coins)
        dp = [[0 for _ in range(l)] for _ in range(l)]

        for i in range(l - 1, -1 ,-1):
            for j in range(i, l):
                if i == j:
                    dp[i][j] == coins[i]
                elif abs(i - j) == 1:
                    dp[i][j] = max(coins[i], coins[j])
                else:
                    dp[i][j] = max(coins[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                                   coins[j] + min(dp[i][j - 2], dp[i + 1][j - 1]))
        
        return dp[0][l - 1]