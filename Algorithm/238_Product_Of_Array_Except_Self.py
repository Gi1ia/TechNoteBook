class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        N = len(nums)
        res = [1 for x in range(N)]
        left, right = 1, 1      
        
        for i in range(N):
            res[i] *= left
            left *= nums[i]
            res[N - 1 - i] *= right
            right *= nums[N - 1 - i]
        
        return res