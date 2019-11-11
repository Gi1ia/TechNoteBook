class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.store = collections.deque()
        self.sum = 0
        self.full = False

    def next(self, val: int) -> float:
        self.store.append(val)
        self.sum += val
        if self.full:
            head = self.store.popleft()
            self.sum -= head
        elif len(self.store) == self.size:
            self.full = True
        
        return float(self.sum/self.size) if self.full else float(self.sum/len(self.store))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)