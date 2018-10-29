class Solution:
    
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num # first is min seen so far (it's a candidate for 1st element)
            elif num <= second: # here when num > first, i.e. num might be either second or third
                second = num # num is better than the current second, store it
            else: # num > first and num > second --> FOUND
                return True
        
        return False
        
        
    def increasingTriplet_TLE(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            while j < len(nums) - 1:
                if nums[i] < nums[j]:
                    k = j + 1
                    print(i, j, k)
                    while k < len(nums):
                        if nums[j] < nums[k]:
                            return True
                        k += 1
                j += 1
            i += 1
        
        return False