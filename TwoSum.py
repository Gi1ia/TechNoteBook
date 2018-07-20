class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        used_nums = {}
        for i in range(0, len(nums)):
            remainder = target - nums[i]
            if remainder in used_nums:
                return [i, used_nums[remainder]]
            else:
                used_nums[nums[i]] = i
        

# debug
if __name__ == '__main__':
    # begin
    s = Solution()
    result = s.twoSum([2, 7, 9, 11], 11)
    print(result)