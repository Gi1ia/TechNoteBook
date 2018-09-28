"""
	Input: candidates = [2,3,5], target = 8,
	A solution set is:
	[
	  [2,2,2,2],
	  [2,3,3],
	  [3,5]
	]
"""
class Sum():
	def combination_sum(self, nums, target):
		#TODO: valid input and edge case
		if not nums:
			return []

		res = []
		self.add_num(nums, target, [], res, 0)
		return res

	def add_num(self, nums, target, current, res, position):
		if target < 0:
			return

		if target == 0:
			res.append(current)
			return

		# target > 0
		for i in range(position, len(nums)):
			current.append(nums[i])
			self.add_num(nums, target - nums[i], current, res, position)
			current.pop()
