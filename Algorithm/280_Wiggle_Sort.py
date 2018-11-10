class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        should_small = True
        for i in range(len(nums) - 1):
            if should_small:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
            should_small = not should_small
            
        
    def wiggleSort_partition(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        N = len(nums)
        mid = self.partition(nums, 0, N - 1, N//2)
        # TODO: Finish partition approach
        
    
    def partition(self, nums, l, r, rank):
        candidate = l
        
        while l < r:
            if nums[l] < nums[r]:
                nums[candidate], nums[l] = nums[l], nums[candidate]
                candidate += 1
            l += 1
        
        nums[candidate], nums[r] = nums[r], nums[candidate]
        
        if candidate == rank:
            return nums[candidate]
        elif candidate > rank:
            return self.partition(nums, l, candidate, rank)
        else:
            return self.partition(nums, candidate + 1, r, rank)