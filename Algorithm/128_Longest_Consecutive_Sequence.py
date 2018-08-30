class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		nums_pool = set(nums)
		res = 0

		for i in range(len(nums)):

			# we only look for the first number in a consecutive sequence.
			# so if we can find a smaller number in the set, we are not going to start counting.
			if nums[i] - 1 not in nums_pool:
				current = nums[i]
				while current in nums_pool:
					current += 1
				res = max(res, current - nums[i])

		return res
		