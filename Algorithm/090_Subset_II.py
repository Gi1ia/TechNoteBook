# FB
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[ [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []]
"""
import collections

class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        res = []
        self.find(nums, [], 0, res)
        return res

    def find(self, nums, path, pos, res):
        res.append(path[:])
        
        for i in range(pos, len(nums)):
            # De-dep.
            if i > pos and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.find(nums, path, i + 1, res)
            path.pop()

s = Solution()
nums = [1,2,2]
print(s.subsetsWithDup(nums))