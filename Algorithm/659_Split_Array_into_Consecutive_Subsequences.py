from collections import Counter
"""
    You are given an integer array sorted in ascending order (may contain duplicates), 
    you need to split them into several subsequences, where each subsequences consist of 
    at least 3 consecutive integers. Return whether you can make such a split.

    Example 1:
    Input: [1,2,3,3,4,5]
    Output: True
    Explanation:
    You can split them into two consecutive subsequences : 
    1, 2, 3
    3, 4, 5
    Example 2:
    Input: [1,2,3,3,4,4,5,5]
    Output: True
    Explanation:
    You can split them into two consecutive subsequences : 
    1, 2, 3, 4, 5
    3, 4, 5
    Example 3:
    Input: [1,2,3,4,4,5]
    Output: False
    Note:
    The length of the input is in range of [1, 10000]
"""

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