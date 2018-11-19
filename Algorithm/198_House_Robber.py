class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        N = len(nums)
        if N < 3:
            return max(nums)
        
        # dp = [0 for _ in range(len(nums))]
        dp = [0 for _ in range(3)]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, N):
            # dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            dp[i%3] = max(dp[(i - 1)%3], dp[(i - 2)%3] + nums[i])
        
        # return dp[-1]
        return dp[(N - 1)%3]