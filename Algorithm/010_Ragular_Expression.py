class Solution:
    def __init__(self):
        self.cache = {}
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = [[False for _ in range(len(s) + 1)] for _ in range(len(p) + 1)]       
        memo[0][0] = True
        
        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous.
        for i in range(2, len(p) + 1):
            memo[i][0] = memo[i - 2][0] and p[i - 1] == '*'
        
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] in {s[j], '.'}:
                    memo[i + 1][j + 1] = memo[i][j]
                if p[i] == '*':
                    if p[i - 1] not in {s[j], '.'}:
                        memo[i + 1][j + 1] = memo[i - 1][j + 1] # Don't touch s. Keep compare s at the same position
                    else:
                        # 1. memo[i + 1][j]: aa -- a* 
                        # 2. memo[i - 1][j + 1]: Eliminate the .* in pattern
                        memo[i + 1][j + 1] = memo[i + 1][j] or memo[i - 1][j + 1]
                
        return memo[-1][-1]       
    
    def isMatch_top_down(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self._dp(s, p, 0, 0)       
        
    def _dp(self, s, p, i, j):
        if (i, j) in self.cache:
            return self.cache[(i, j)]
        
        res = False
        if j == len(p):
            res = i == len(s)
        
        else:        
            first_match = False
            if i < len(s) and p[j] in {s[i], '.'}:
                first_match = True

            if j + 1 < len(p) and p[j + 1] == '*':
                res = self._dp(s, p, i, j + 2) or (first_match and self._dp(s, p, i + 1, j))
            else:
                res = first_match and self._dp(s, p, i + 1, j + 1)

            self.cache[(i, j)] = res
        
        return res  


    def isMatch_recursive(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        first_match = False
        if len(s) > 0 and p[0] in { s[0], '.'}:
            first_match = True
        
        if len(p) > 1 and p[1] == '*':             
                # eliminate .* in p; compare rest of the string
                return self.isMatch(s, p[2:]) \
                or (first_match and self.isMatch_recursive(s[1:], p)) # e.g. aaaaa <--> a*
        
        else:
            return first_match and self.isMatch_recursive(s[1:], p[1:])
        

# ref: https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
# https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest