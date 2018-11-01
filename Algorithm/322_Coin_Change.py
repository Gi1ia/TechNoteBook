class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins:
            return -1
        
        # dp[i] means least coins we can choose to make money i
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for j in range(len(coins)):
                if coins[j] <= i: # coins could be candidate
                    # HOW TO HANDLE MULTIPLE COINS?
                    # Instead of using:
                    # f(i, j) = min(f(i - 1, j), f(i - 1, j - coins[i] * k) + k)
                    # We use:
                    # f(i, j) = min(f(i - 1, j), f(i, j - coins[i]) + 1)
                    # Since f(i-1, j) should be equal to f(i, j) (we don't choose the coin)
                    # we have following formula
                    dp[i] = min(dp[i - coins[j]] + 1, dp[i])
        
        return -1 if dp[amount] == float('inf') else dp[amount]
                    
            
                
                
        