from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            # push the num into samll, then grab the largest in samll and push it into large
            heappush(self.large, -heappushpop(self.small, -num)) 
        else:
            heappush(self.small, -heappushpop(self.large, num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small) == len(self.large):
            return (self.large[0] - self.small[0]) / 2
        else:
            # we always push num to large first, it has the larger halp
            return float(self.large[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()