class Solution:
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

        
        