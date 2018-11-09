"""
    Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
    If there isn't one, return 0 instead.

    Note:
    The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

    Example 1:

    Input: nums = [1, -1, 5, -2, 3], k = 3
    Output: 4 
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
    Example 2:

    Input: nums = [-2, -1, 2, 1], k = 1
    Output: 2 
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.
    Follow Up:
    Can you do it in O(n) time?

    #FB #G #HashTable
"""
class Solution:
    def maxSubArrayLen_I(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        
        acc_sum = {}
        acc_sum[0] = -1 # array sums to 0 == array sums from start
        res = 0
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if (curr_sum - k) in acc_sum:
                res = max(res, i - acc_sum[curr_sum - k])
            if curr_sum not in acc_sum:
                acc_sum[curr_sum] = i
        
        return res
    
    def maxSubArrayLen_II(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        if not nums:
            return 0
        
        l = len(nums)
        acc = [0 for x in range(l)]
        accMap = {}
        res = 0
        
        accMap[0] = -1 # if a acc[i] == 0, we can regard it was from start of the array
        
        for i in range(l):
            if i == 0:
                acc[i] = nums[i]
            else:
                acc[i] = acc[i - 1] + nums[i]
            if acc[i] not in accMap:
                accMap[acc[i]] = i
        
        for i in range(l):
            if acc[i] - k in accMap:
                res = max(res, i - accMap[acc[i] - k])
            
        
        return res

s = Solution()
nums = [-2, -1, 2, 1]
nums2 = [-1,1]
print(s.maxSubArrayLen_I(nums2, 0))
