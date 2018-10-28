class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        nums.sort()
        
        pair_map = collections.defaultdict(list)
        res = set()
        
        for i in range(len(nums)):
            if i > 1 and nums[i] == nums[i - 2]: # why 2?
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 2 and nums[j] == nums[j - 2]: # why 2?
                    continue
                    
                # Check the target - pair 
                if target - nums[i] - nums[j] in pair_map:
                    pair_list = pair_map[target - nums[i] - nums[j]]
                
                    for pair in pair_list:
                        tmp1 = min(pair[0], i)
                        tmp2 = min(pair[1], j)
                        tmp3 = max(pair[0], i)
                        tmp4 = max(pair[1], j)

                        # two pair are the same. de-dup
                        if tmp1 == tmp3 or tmp2 == tmp4 or tmp1 == tmp4 or tmp2 == tmp3:
                            continue

                        current = (nums[tmp1], nums[min(tmp2, tmp3)], nums[max(tmp2, tmp3)], nums[tmp4])
                        res.add(current)                
                
                pair_map[nums[i] + nums[j]].append((i, j))
        
        return list(res)
                
                    
                
    