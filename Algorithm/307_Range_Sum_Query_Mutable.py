class NumArray_bottom_up(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = len(nums)
        if self.N > 0:        
            self.seg_tree = [0 for _ in range(2 * self.N)]
            self._build_seg_tree(nums)
        else:
            self.seg_tree = [0]       
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        # find out the item index in seg_tree
        pos = i + self.N
        self.seg_tree[pos] = val

        # below is the general way to update node
        # if we only store sum like this question,
        # we don't need to look at left/right node,
        # we could use diff and update i /= 2 all the way up.
        # see # 9801 as example.
        while pos > 0: # we don't use index 0
            left, right = pos, pos
            if pos % 2 == 0:
                right += 1 # pos has a right neighbor
            else:
                left -= 1 # pos has a left neighbor
            
            # Update parent node
            pos //= 2
            self.seg_tree[pos] = self.seg_tree[left] + self.seg_tree[right]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        # get the real index in seg_tree
        left, right = i + self.N, j + self.N
        sum = 0
        while left <= right:
            if left % 2 == 1: # left boundry is a right node => its parent node won't help
                sum += self.seg_tree[left]
                left += 1
            if right % 2 == 0: # right boundry is a left node
                sum += self.seg_tree[right]
                right -= 1
            left //= 2
            right //= 2
        
        return sum
        
    
    def _build_seg_tree(self, nums):
        for i in range(self.N):
            self.seg_tree[i + self.N] = nums[i]
        for i in range(self.N - 1, 0, -1): # we won't use index 0
            self.seg_tree[i] = self.seg_tree[i * 2] + self.seg_tree[i * 2 + 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)