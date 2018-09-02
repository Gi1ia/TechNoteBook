import math

class Solution:
    def numSquares_BFS(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Create a list that contains 1, 4, 9, ... k**2 <= n
        s = []
        i = 1
        while i * i <= n:
            s.append(i * i)
            i += 1

        # initialize
        level = 0
        to_check = {n}

        while to_check:
            level += 1
            # Temp is used to refresh the queue.
            # Since we need to record the level #, we can not fill the queue while we iterate elements.
            # We iterate each level first, then replace the queue for next level.
            temp = set()
            for x in to_check:
                for y in s:
                    if x == y:
                        return level
                    if x < y:
                        break
                    temp.add(x - y)
            to_check = temp

        return level

s = Solution()
print(s.numSquares_BFS(12))
