class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        N = len(nums)
        dp = [[0 for i in range(N + 2)] for i in range(N + 2)]
        nums.append(1)
        nums.insert(0, 1)

        for j in range(1, N + 1):
            for i in range(j, 0, -1):
                for k in range(i, j + 1):
                    current = nums[i - 1] * nums[j + 1] * nums[k]
                    dp[i][j] = max(dp[i][j], dp[i][k - 1] + dp[k + 1][j] + current)

        return dp[1][N]

nums = [3, 1, 5, 8]
obj = Solution()
print(obj.maxCoins(nums))                        
                