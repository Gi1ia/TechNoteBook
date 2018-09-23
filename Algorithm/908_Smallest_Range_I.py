class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return 0
        
        l = len(A)
        if l == 1:
            return 0
        
        
        A = sorted(A)
        if abs(A[0] - A[-1]) <= K * 2:
            return 0
        
        res = A[-1] - A[0] - K * 2
        return res