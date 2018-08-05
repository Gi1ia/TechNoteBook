"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
 find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
#Facebook #Google #Snapchat #Heap #Greedy
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int

        # Very similar with what we do in real life. Whenever you want to start a meeting, 
        # you go and check if any empty room available (available > 0) and
        # if so take one of them ( available -=1 ). Otherwise,
        # you need to find a new room someplace else ( numRooms += 1 ).  
        # After you finish the meeting, the room becomes available again ( available += 1 ).
        """
        if not intervals:
            return 0

        # Considering the room as resources, if start[s] < end[e], 
        # it means we do not have available resource now. Otherwise, 
        # it means when you are starting a new conferences, 
        # some other ones have finished, 
        # i.e., we have available resource already. 

        # You do not really care about the meeting that the start and end time belong to, 
        # and no need to preserve their relationship.
        
        starts = [intervals.start for interval in intervals]
        ends = [intervals.end for interval in intervals]

        starts.sort()
        ends.sort()

        i = j = 0
        max_rooms = available_rooms = 0

        while i < len(starts):
            if starts[i] < ends[j]:
                available_rooms += 1
                i += 1
            elif starts[i] > ends[j]:
                j += 1
                available_rooms -= 1
            else:
                i += 1
                j += 1
            max_rooms = max(max_rooms, available_rooms)
        
        return max_rooms

        