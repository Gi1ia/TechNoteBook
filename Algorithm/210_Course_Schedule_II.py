"""
There are a total of n courses you have to take, labeled from 0 to n-1.
Some courses may have prerequisites, for example to take course 0 you have 
to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, 
return the ordering of courses you should take to finish all courses.
There may be multiple correct orders, you just need to return one of them. 
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
"""
import collections

class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # TODO Valid input; Need to confirm that there is no single point in the graph.
        res = []
        outdegree = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for follow, pre in prerequisites:
            outdegree[pre].append(follow)
            indegree[follow] += 1
        
        q = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            # For Course_Schedule_I, count how many course we can pop from queue
            # if @count == numCourses, return True
            course = q.popleft()
            res.append(course)
            for j in outdegree[course]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        return res if len(res) == numCourses else []    
                     
        