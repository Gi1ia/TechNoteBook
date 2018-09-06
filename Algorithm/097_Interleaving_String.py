class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        if s1[-1] == s3[-1], then isInterleave(s1, s2, s3) == isInterleave(s1[:-1], s2, s3)
        if s2[-1] == s3[-1], isInterleave(s1, s2, s3) == isInterleave(s1, s2[:-1], s3)
        define: dp[i][j] means s1[0, i] and s2[0, j] map to s3[0, i + j]
        """
        # TODO: Need to solve this problem again...
        if len(s3) != len(s1) + len(s2):
            return False
        
        dp = [[None for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = False
        
        for j in range(1, len(s2) + 1):
            if s2[j - 1] == s3[j - 1]:
                dp[0][j] = dp[0][j - 1]
            else:
                dp[0][j] = False
            
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                dp[i][j] = (s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]) \
                or (s2[j - 1] == s3[i + j - 1] and dp[i][j - 1])
        
        return dp[len(s1)][len(s2)]

s1, s2 = "aabcc", "dbbca"
s3 = "aadbbcbcac"
s = Solution()
print(s.isInterleave(s1, s2, s3))