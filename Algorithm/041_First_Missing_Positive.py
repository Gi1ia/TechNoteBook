class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        l = len(nums)
        for i in range(len(nums)):
            # Note: we use while because we need to keep loop until we reach the correct ans
            # we want to put A[i] into No.i - 1 index if A[i] is valid
            # for every index i - 1, we want to it store i ==>
            # A[i - 1] = i ==>
            # A[f(x) - 1] = f(x)
            while nums[i] > 0 and nums[i] <= l and nums[nums[i] - 1] != nums[i]:
                self.swap(nums, i, nums[i] - 1) # need to extract as a seperate function
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1
        
    
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]