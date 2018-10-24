class Node():
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None
        self.sum = 0

class WaterDeep(): # SegmentTree
    def __init__(self, nums):
        if not nums:
            return
        self.nums = nums
        self.N = len(nums)
        # self.root = Node()
        self.store = [0 for _ in range(2 * N)]
        self._build()
    
    def look(self, n):
        i = 1

        while i < len(nums):
            if i >= self.N: # reach the bottom
                break
            if n < self.store[i]:
                i = i * 2
            elif n > self.store[i]:
                n -= store[i]
                i = i * 2 + 1

        return i - N

    def set_height(self, order, new_height):
        position = self.N + order # looking for real position in store
        i = position
        diff = self.store[position] - new_height
        while i > 0:
            self.store[i] -= diff
            i = i // 2

    def _build(self):
        for i in range(N):
            self.store[N + i] = self.nums[i]

        for i in range(N - 1, 0, -1):
            self.store[i] = self.store[i * 2] + self.store[i * 2 + 1]
  



