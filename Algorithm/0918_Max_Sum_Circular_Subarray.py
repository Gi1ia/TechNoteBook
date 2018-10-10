class Solution:
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        
        N = len(A)
        
        res = A[0]
        current = 0
        
        # 1-interval sum
        for num in A:
            current += num
            res = max(res, current)
            current = max(0, current)
            
        # 2-interval sum
        
        # rightsum[i] = sum(A[i:])
        rightsums = [None] * N
        rightsums[-1] = A[-1]
        for i in range(N - 2, -1, -1):
            rightsums[i] = rightsums[i + 1] + A[i]
            
        # maxright[i] = max_{j >= i} rightsums[j]
        maxright = [None] * N
        maxright[-1] = rightsums[-1]
        for i in range(N - 2, -1, -1):
            maxright[i] = max(maxright[i + 1], rightsums[i])
        
        leftsum = 0
        for i in range(N - 2):
            leftsum += A[i]
            # we use i + 2 because if we calculate i, i + 1, i + 2,
            # it will become the entire array sum,
            # which we calculated above
            res = max(res, leftsum + maxright[i + 2]) 
        return res

s = Solution()
nums = [5, -2, 5]
print(s.maxSubarraySumCircular(nums))