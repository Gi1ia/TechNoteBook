"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[[2,4],
[3,4],
[2,3],
[1,2],
[1,3],
[1,4],]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if not n or k > n:
            return []
        
        res = []
        self.find(n, k, [], res, 1)

        return res

    def find(self, n, k, path, res, pos):
        # prune
        # If the elements left in n is not enough to form a result
        # return here
        if n - pos + 1 < k - len(path):
            return

        if len(path) == k:
            res.append(path[:])
            return
        
        for i in range(pos, n + 1):
            path.append(i)
            self.find(n, k, path, res, i + 1)
            path.pop()

s = Solution()
print(s.combine(4, 2))