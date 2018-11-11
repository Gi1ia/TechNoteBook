class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        # Another approach using 2d dp
        # https://buptwc.github.io/2018/11/11/Leetcode-940-Distinct-Subsequences-II/
        
        dp = [1] # empty S will have 1 ("") subset
        
        # Count last time when we added char to the previous result
        # What state (dp[i]) we were at
        # Here, that dp[i] is the count we want to remove
        # because last time we add x at index i, we already based on dp[i], and made the move
        last = {} 
        
        for i, x in enumerate(S):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
                
            last[x] = i
        
        return (dp[-1] - 1)%(10**9 + 7) # to exclude the empty ""