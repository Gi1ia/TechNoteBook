class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (not word1) and (not word2):
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        
        distance = [[0 for _ in range(len(word2) + 1)]\
                    for _ in range(len(word1) + 1)]
        
        # Initialize dp cache
        for i in range(len(word1) + 1):
            distance[i][0] = i
        
        for j in range(len(word2) + 1):
            distance[0][j] = j
        
        for x in range(1, len(word1) + 1):
            for y in range(1, len(word2) + 1):
                # If letters at word11[i] and word2[j] are equal,
                # we don't need step to change it
                if word1[x - 1] == word2[y - 1]:
                    distance[x][y] = distance[x - 1][y - 1]
                else:
                    # If the letters are not the same, we could
                    # 1) In the case that length is equal, change the letter
                    # thus, the we need 1 step from distance[x - 1][y - 1]
                    # 2) length are not the same, add/delete letter,
                    # we need 1 step from distance[x - 1][y] or distance[x][y - 1]
                    distance[x][y] = 1 + min(distance[x - 1][y],\
                     distance[x][y - 1], distance[x - 1][y - 1])
        
        return distance[-1][-1]

s = Solution()
str1 = "horse"
str2 = "ors"
print(s.minDistance(str1, str2))