"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. 
If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time 
complexity is O(n log n). 
"""

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        temp_sum = 0
        res = float("inf")
        j = 0
        for i in range(len(nums)):
            temp_sum += nums[i]
            while temp_sum >= s: # note: use while so we can find out shortest
                res = min(res, i - j + 1)
                temp_sum -= nums[j]
                j += 1
            
        return res if res != float("inf") else 0
                