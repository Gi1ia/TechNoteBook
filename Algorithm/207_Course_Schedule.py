import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not numCourses or numCourses == 0:
            return True
        
        indegree = [0 for _ in range(numCourses)]
        outdegree = collections.defaultdict(list)
        
        for pre, follow in prerequisites:
            outdegree[pre].append(follow)
            indegree[follow] += 1
        
        q = collections.deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            current = q.popleft()
            res.append(current)
            if outdegree[current]:
                for j in outdegree[current]:
                    indegree[j] -= 1
                    if indegree[j] == 0:
                        q.append(j)
        
        return len(res) == numCourses
                    