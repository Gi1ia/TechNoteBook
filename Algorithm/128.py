class Al():
	"""docstring for Al"""
	def lcs(self, nums):
		"""
		"""
		nums_pool = set(nums)
		res = 0
		for i in range(len(nums)):
			if nums[i] - 1 not in nums_pool:
				current = nums[i]
				while current in nums_pool:
					current += 1
				res = max(res, current - nums[i])

		return res
		