class Solution:
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        small = A[0]
        large = A[-1]
        res = large - small
        
        for i in range(len(A) - 1):
            left, right = A[i], A[i + 1]
            res = min(res, max(large - K, left + K) - min(right - K, small + K))
        return res