class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        
        left, right = 0, len(nums) - 1
        bottom, ceiling = -1, -1
        
        # find bottom
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
                
        if nums[left] == target:
            bottom = left
        elif nums[right] == target:
            bottom = right
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid

        if nums[right] == target:
            ceiling = right
        elif nums[left] == target:
            ceiling = left
                
        return [bottom, ceiling]