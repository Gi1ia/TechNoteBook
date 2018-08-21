class Solution():
    def max_subarray(self, nums):
        if not nums or len(nums) == 0:
            return 0
        
        max_sum = nums[0]
        current_sum = 0

        for i in range(0, len(nums)):
            current_sum += nums[i]
            max_sum = max(max_sum, current_sum)
            current_sum = max(0, current_sum)
        
        return max_sum