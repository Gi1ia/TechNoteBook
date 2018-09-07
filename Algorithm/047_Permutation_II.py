class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        
        nums.sort()
        used = [False for _ in range(len(nums))]
        res = []
        self.find(nums, [], res, used)

        return res

    def find(self, nums, path, res, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            # The second condition means, we won't 
            # insert the second char in a duplicated sequence
            # However, we need to permute all the same char,
            # so we have condition `used[i - 1] == True`
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            path.append(nums[i])
            used[i] = True
            self.find(nums, path, res, used)
            used[i] = False
            path.pop()
            
s = Solution()
nums = [1,1,2]
print(s.permuteUnique(nums))