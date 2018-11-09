"""
    There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

    Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

    Example 1:
    Input: 
    [[1,1,0],
    [1,1,0],
    [0,0,1]]
    Output: 2
    Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
    The 2nd student himself is in a friend circle. So return 2.
"""

import collections

class Solution:
    # It can all be done in union find
    def findCircleNum_bfs(self, M):
        if not M or not M[0]:
            return 0
        
        visited = [0 for x in range(len(M))]
        count = 0
        friend_circle = collections.deque([])
        
        for i in range(len(M)):
            if visited[i] == 0:            
                friend_circle.append(i)              
                while len(friend_circle) > 0:
                    temp = friend_circle.popleft()
                    visited[temp] = 1
                    for j in range(len(M)):
                        # Note: Remeber here we want to look at M[temp][j], do not look at M[i][j] anymore.
                        if M[temp][j] == 1 and visited[j] == 0:
                            friend_circle.append(j)
                count += 1
        
        return count

    def findCircleNum_dfs(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        Note: Even the input is a 2d list, 
        in fact we only care about if a people has been found in friend circle or not.
        So we can maintain a list contains visited status of a people, and use DFS to transverse all the links.
        """
        if not M or not M[0]:
            return 0
        
        visited = [0 for x in range(len(M))]
        count = 0
        
        for i in range(len(M)):
            if visited[i] == 0:
                self.findFriend(M, visited, i)
                count += 1
        
        return count
    
        
    def findFriend(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.findFriend(M, visited, j)
        

s = Solution()

        
        