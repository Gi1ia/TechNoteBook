class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        left is the rightmost boundary of 0
        right is leftmost boundary of 2
        swap current with left/right regard of it's value
        """
        left = current = 0
        right = len(nums) - 1
        
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1