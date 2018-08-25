"""
There are n coins in a line. (Assume n is even). 
Two players take turns to take a coin from one of the ends of the line until there are no more coins left. 
The player with the larger amount of money wins.

1. Would you rather go first or second? Does it matter?
2. Assume that you go first, describe an algorithm to compute the maximum amount of money you can win. 
"""

class Solution(object):
  def coin_in_a_line(self, coins):
    """
    :param coins: List[int]
    :return: Boolean
    """
    if not coins:
      return True
    if len(coins) <= 2:
      return True
​
    l = len(coins)
    sum_value = [[0 for x in xrange(l)] for x in xrange(l)]
    dp_res = [[0 for x in xrange(l)] for x in xrange(l)]
​
    # initial sum_value list
    for i in xrange(l):
      for j in xrange(i, l):
        if i == j:
          sum_value[i][j] = coins[i]
        else:
          sum_value[i][j] = coins[j] + sum_value[i][j - 1]
​
    for i in xrange(l - 1, -1, -1):
      for j in xrange(i, l):
        if i == j:
          dp_res[i][j] = coins[i]
        else:
          dp_res[i][j] = sum_value[i][j] - min(dp_res[i + 1][j], dp_res[i][j - 1])
​
    return dp_res[0][l - 1] > sum_value[0][l - 1] - dp_res[0][l - 1]
​
s = Solution()
test = s.coin_in_a_line([1, 20, 4])
test2 = s.coin_in_a_line([1, 2, 4])
print test2
