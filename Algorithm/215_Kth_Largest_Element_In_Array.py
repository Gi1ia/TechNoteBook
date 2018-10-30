class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        
        pos = self.partition(nums, 0, len(nums) - 1)
        if pos > k - 1:
            return self.findKthLargest(nums[:pos], k)
        elif pos < k - 1:
            return self.findKthLargest(nums[pos + 1:], k - pos - 1)
        else:
            return nums[pos]
        
    
    def partition(self, nums, l, r):
        candidate = l # r will be pivot value
        
        while l < r:
            if nums[l] > nums[r]: # this partition will put large number in front
                nums[candidate], nums[l] = nums[l], nums[candidate]
                candidate += 1
            l += 1
        
        nums[candidate], nums[r] = nums[r], nums[candidate]
        return candidate #pivot