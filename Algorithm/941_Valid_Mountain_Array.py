class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i, j = 0, len(A) - 1
        
        while i < len(A) - 1 and A[i] < A[i + 1]:
            i += 1
        while j > 0 and A[j] < A[j - 1]:
            j -= 1
        
        return 0 < i == j < len(A) - 1
        