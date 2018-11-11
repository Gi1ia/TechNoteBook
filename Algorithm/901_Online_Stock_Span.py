class StockSpanner(object):

    def __init__(self):
        self.dp = []
        self.cursor= 0
        self.history = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        # Idea is, use dp[] to store how many consecutive price before current is smaller
        # Then jump over those range, and do next compare

        if self.cursor == 0 or price < self.history[-1]:
            self.dp.append(1) # no consecutive price before current is smaller
        else:
            i = self.cursor - 1
            # NOTE: if price is equal, it's legal to count
            while i >= 0 and price >= self.history[i]:
                i -= self.dp[i]
            self.dp.append(self.cursor - i)
        
        self.cursor += 1
        self.history.append(price)
        return self.dp[-1]
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)