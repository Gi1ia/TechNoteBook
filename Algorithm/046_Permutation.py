class Solution(object):
    def __init__(self):
        self.res = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        if len(nums) == 1:
            return [nums]
        
        for i, e in enumerate(nums):
            temp = nums[:i] + nums[i + 1:]
            lists = self.permute(temp)
            for l in lists:
                l.append(e)
                self.res.append(l[:])
        return self.res

    def permute_backtrack(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        
        self.find(nums, [], self.res)
        return self.res
    
    def find(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
        
        for n in nums:
            if n in path:
                continue
            path.append(n)
            self.find(nums, path, res)
            path.pop()