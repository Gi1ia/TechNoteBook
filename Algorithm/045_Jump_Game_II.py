class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums or len(nums) == 1:
            return 0

        left, right = 0, 0
        step = 0
        
        # Try to reach as far as we can in the range
        while left <= right:
            old_right = right
            step += 1
            # we want to try nums[old_right], thus the range is (left, old_right + 1)
            for i in range(left, old_right + 1):
                right = max(i + nums[i], right)
                
                # we win by reach the last index, not finish entire nums.
                if right >= len(nums) - 1:
                    return step
            # Move left boundry of the range
            left = old_right + 1
        
        return 0