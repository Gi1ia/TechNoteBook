"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals or len(intervals) < 2:
            return intervals
        
        intervals.sort(key = lambda x: x.start)
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            current = stack.pop()
            if current.end >= intervals[i].start:
                merged = self.merge_two(current, intervals[i])
                stack.append(merged)
            else:
                stack.append(current) # push previous interval back
                stack.append(intervals[i])

        return stack
        
    def merge_two(self, i1, i2):
        new_start = min(i1.start, i2.start)
        new_end = max(i1.end, i2.end)
        return Interval(new_start, new_end)
        