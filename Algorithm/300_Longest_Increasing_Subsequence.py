class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		if len(nums) <= 1:
			return len(nums)

		# Current[i] will store the length of LIS that end with nums[i]
		current = [1 for _ in range(len(nums))]
		for i in range(1, len(nums)):
			for j in range(0, i):
				# It means nums[i] can contribute to current[j] by 1
				# And the new LIS will end with nums[i]
				if nums[j] < nums[i]:
					current[i] = max(current[i], current[j] + 1)

		return max(current)