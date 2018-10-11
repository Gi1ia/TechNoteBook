"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.
"""
import collections
class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        
        res = []
        
        # maintain a deque, it has all candidates that could be current max
        # and its left side is bigger than right side 
        # thus, we always choose candidates current[0]
        current = collections.deque()
        for i, n in enumerate(nums):
            # make sure the right side of current is smallest
            # if nums[current[-1]] <= n, we discard candidate at current[-1] 
            # if nums[current[-1]] > n, we simply add n as a candidate
            while current and n >= nums[current[-1]]:
                current.pop()
            
            current.append(i) # Add candidate
            
            if i - current[0] >= k: # keep current in bound
                current.popleft()
            
            if i + 1 >= k:
                res.append(nums[current[0]])
            
        return res
            