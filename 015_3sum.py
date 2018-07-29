"""
Given an array S of n integers, are there elements a, b, c in S such that a +
b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},
    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution(object):
    def threeSum_no_deDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :Note: This solution will contain duplicated answer. 
        """
        nums.sort()

        # if we change res to a set: res = set()
        # and return the set in list format, the de-dup problem will be solved.
        # 1. return list(res)
        # 2. return map(list, res)
        res = []
        
        for i in range (0, len(nums) - 2): # exclude last two indexes
          if i > 0 and nums[i] == nums[i - 1]: # first index should be identical
            continue
          left = i + 1
          right = len(nums) - 1
          while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < 0:
              left += 1
            elif current_sum > 0:
              right -= 1
            else:
              res.append((nums[i], nums[left], nums[right]))
              left += 1
              right -= 1
        
        return res

    def threeSum(self, nums):
      """
        :type nums: List[int]
        :rtype: List[List[int]]
      """
      nums.sort()
      res = []

      for i in range (0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
          continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
          current_sum = nums[i] + nums[left] + nums[right]
          if current_sum < 0:
            left += 1
          elif current_sum > 0:
            right -= 1
          else:
            res.append((nums[i], nums[left], nums[right]))
            # by checking the next index value to solve de-dup.
            while left < right and nums[left] == nums[left + 1]:
              left += 1
            while left < right and nums[right -1] == nums[right]:
              right -= 1
            # Note: Following code is for normal cases. 
            # Without the following line, the loop will be infinite.
            left, right = left + 1, right - 1
      
      return res

s = Solution()
print (s.threeSum([-2,0,0,2,2]))
print (s.threeSum_no_deDup([-2,0,0,2,2]))
input("Press Enter")