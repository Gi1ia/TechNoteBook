"""
Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
"""

class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        
        days = len(prices)
        buy = [0 for _ in range(days)]
        sell = [0 for _ in range(days)]
        buy[0] = -prices[0]

        for i in range(1, days):
            # stock > 0 day
            # in day i, we buy or hold stock (do nothing)
            # in order to buy stock, we need to sell stock on day i - 1
            buy[i] = max(sell[i - 1] - prices[i], buy[i - 1])
            # stock == 0 day
            # in day i, we sell stock, or we don't buy stock (do nothing)
            # Also, remember to deduct fee when selling stock
            sell[i] = max(buy[i - 1] + prices[i] - fee, sell[i - 1])

        
        return sell[days - 1]