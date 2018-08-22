class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        
        
        # assign left as 0, right can be last item or out of boundary
        left = 0
        right = len(nums)
        
        # initialize middle as 0
        middle = 0
        
        # when left == right, break out
        while(left < right):
            # remeber it's always left bias
            middle = left + (right - left)//2
            
            # if target is located at second half, should go beyound middle point to avoid dead loop.
            if target > nums[middle]:
                left = middle + 1
                middle += 1
            else:
                right = middle
                
        # Return left or middle both works.
        # First is better because no need to keep tracking middle
        return left