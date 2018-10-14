"""
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Note:
schedule and schedule[i] are lists with lengths in range [1, 50].
0 <= schedule[i].start < schedule[i].end <= 10^8.
"""
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

import heapq
class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        res = []
        h = []
        last_end = float("inf")
        
        # push first working time of each employee into heap
        for index, employee_times in enumerate(schedule):
            if employee_times:
                # item is (start_time of working_time, employee_index, employee working_time)
                item = (employee_times[0].start, index, 0)
                heapq.heappush(h, item)
            last_end = min(last_end, employee_times[0].end)
                
        while h:
            start_time, employ_id, time_id = heapq.heappop(h)
            if start_time > last_end:
                res.append(Interval(last_end, start_time))
                
            last_end = max(last_end, schedule[employ_id][time_id].end)
            if time_id +1 < len(schedule[employ_id]):
                # Node: remember to push the new value into heap
                item = (schedule[employ_id][time_id + 1].start, employ_id, time_id + 1)
                heapq.heappush(h, item)
                
            
        return res