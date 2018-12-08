"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
"""

class Solution:
    # TODO: Solve the problem in O(1) space
    def maxProfit_StateMachine(self, prices):
        """
        O(1) space
        """
        if not prices:
            return 0

        # s0 is do nothing
        s1 = -prices[0] # s1 is the cost to buy stock
        s2, s3, s4 = float('-inf'), float('-inf'), float('-inf')

        # ssume we are in state S
        # if we buy, we are spending money but we can also choose to do nothing
        # Doing nothing means going from S->S
        # Buying means going from some state X->S, losing some money in the process

        for i in range(len(prices)):
            s1 = max(s1, -prices[i])
            s2 = max(s2, s1 + prices[i])
            s3 = max(s3, s2 - prices[i])
            s4 = max(s4, s3 + prices[i])
        
        return max(0, s4)

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :Time complexity == O(n)
        """
        if not prices:
            return 0
        
        days = len(prices)
        # We are looking for max(profit(0, i) + profit(i, days)) where i in range(0, days)
        profit1 = [0 for _ in range(days)] # First transition profit
        profit2 = [0 for _ in range(days + 1)] # Second transition profit
        
        lowest_so_far = prices[0]
        first_profit = 0
        for i in range(days):
            lowest_so_far = min(prices[i], lowest_so_far)
            first_profit = max(first_profit, prices[i] - lowest_so_far)
            profit1[i] = first_profit
        
        highest_so_far = prices[-1]
        second_profit = 0
        for i in range(days - 1, -1, -1):
            highest_so_far = max(highest_so_far, prices[i])
            second_profit = max(second_profit, highest_so_far - prices[i])
            profit2[i] = second_profit
            
        res = 0
        for i in range(days):
            # we could sell and buy stock at the same day,
            # which means we do nothing on that day
            # e.g. we only buy and sell stock once 
            res = max(res, profit1[i] + profit2[i]) 
        
        return res