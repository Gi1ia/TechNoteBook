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
            