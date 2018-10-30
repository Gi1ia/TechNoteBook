from collections import Counter

class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # store how many num we can still use
        count = Counter(nums)
        
        # store subsequency (chain) we've made that end with x - 1
        # which means they are ready to append x to the end of it.
        tails = Counter()
        
        for num in nums:
            if count[num] == 0:
                continue
            elif tails[num] > 0:
                tails[num] -= 1 # prev chain end with x - 1 no longer exit because we add x to it
                tails[num + 1] += 1
            elif count[num + 1] and count[num + 2]: # we start a new chain only if the chain could longer than 3
                count[num + 1] -= 1
                count[num + 2] -= 1
                tails[num + 3] += 1
            else:
                return False
            
            count[num] -= 1 # use the num, minus one from count anyway
        
        return True