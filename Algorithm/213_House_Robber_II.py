"""
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
"""

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Basic idea: since the houses are in a circle, 
        # the only edge case is rob the last one and the first one at same time.
        # So we split the nums into [:-1] and [1:] to solve the problem
        if not nums:
            return 0
        N = len(nums)
        if N < 4:
            return max(nums)
        
        return max(self.rob_row(nums[:-1]), self.rob_row(nums[1:]))
    
    def rob_row(self, nums):
        dp = [0, 0, 0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i%3] = max(dp[(i - 1)%3], dp[(i - 2)%3] + nums[i])
        
        return dp[(len(nums) - 1)%3]