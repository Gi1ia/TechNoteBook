"""
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Each number in candidates may only be used once in the combination.
"""

class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        
        candidates.sort()
        res = []
        self.add_num(candidates, target, [], 0, res)
        
        return res
        
    
    def add_num(self, nums, target, current, position, res):
        if target < 0:
            return
        
        if target == 0:
            res.append(current[:])
            return
        
        for i in range(position, len(nums)):
            # edge case: [1, 1, 2, 5, 6] -> 8
            # [1, 1, 6] is fine
            # but we don't want two [1, 2, 5]
            if i > position and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.add_num(nums, target - nums[i], current, i + 1, res)
            current.pop()
        