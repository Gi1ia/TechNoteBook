"""
Given an array of meeting time intervals consisting of start and end times 
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""
# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
                
        return True

    def canAttendMeetings_BruteForce(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        for i in range(0, len(intervals)-1):
            for j in range(i + 1, len(intervals)):
                if self.isOverlap(intervals[i], intervals[j]):
                    return False
        
        return True

    def isOverlap(self, i1, i2):
        """
        :type i1, i2: Interval
        :rtype: bool
        Define
        """
        return (min(i1.end, i2.end) > max(i1.start, i2.start))
