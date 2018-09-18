class Solution:
    def isScramble_DP(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 and not s2:
            return True
        if not s1 or not s2:
            return False
        if len(s1) != len(s2):
            return False
        
        n = len(s1)
        # F[n][i][j] means if s1[i:i + n] and s2[j:j + n] are scramble
        f = [[[False for _ in range(n)] for _ in range(n)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                f[1][i][j] = s1[i] == s2[j]
        
        # iterate length; make l from 1 to n + 1
        for l in range(1, n + 1):
            for i in range(n + 1 - l): # i + l <= n to make sure index is not overflow
                for j in range(n + 1 - l):
                    for split in range(1, l): # split string to check left and right
                        if (f[split][i][j] and f[l - split][i + split][j + split]) or \
                            (f[split][i][j + l - split] and f[l - split][i + split][j]):
                            f[l][i][j] = True
        
        return f[n][0][0]


    def isScramble_TLE(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 and not s2:
            return True

        l = len(s1)
        if l == 1:
            return s1 == s2

        for i in range(1, l): 
            # split the string from index i, and compare 4 strings
            left = self.isScramble_TLE(s1[:i], s2[:i]) and self.isScramble_TLE(s1[i:], s2[i:])
            right = self.isScramble_TLE(s1[:i], s2[(l - i):]) and self.isScramble_TLE(s1[i:], s2[:(l - i)])
            if left or right:
                return True

        return False
        
s1, s2 = "gre", "egr"
s = Solution()
print(s.isScramble_DP(s1, s2))

# Q: Is it permutation?
# A: No.   e.g. great ==> raget