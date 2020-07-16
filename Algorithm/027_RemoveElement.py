"""
Remove all instances of given value in-place and return new length.
nums = [3, 2, 2, 3], val = 3
Return 2, nums in-place change to [2, 2, 3, 3]
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Time O(n) --> 2n; Space: O(1)
        """
        slow = 0

        # If nums[fast] != val, copy it's value to slow pointer
        for fast in range(len(nums)):
            if (nums[fast] != val):
                nums[i] = nums[j]
                slow += 1

        return slow

    def removeElement_swap(self, nums: List[int], val: int) -> int:
        """
        When we encounter nums[i] == val, swap it's value with last element and dispose last one immediatly.
        O(n), swap operation == # of removed elements. So it's faster if removable value is rare.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                n -= 1
            else:
                i += 1
        
        return n
