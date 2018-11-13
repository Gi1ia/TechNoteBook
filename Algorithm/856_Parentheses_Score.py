class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = self._score(S, 0, len(S) - 1)
        
        return res
        
        
    def _score(self, S, l, r):
        if r - l == 1:
            return 1
        
        split = 0
        for i in range(l, r): # ignore the last ), so we split won't be confused
            if S[i] == '(':
                split += 1
            if S[i] == ')':
                split -= 1
            if split == 0:
                return self._score(S, l, i) + self._score(S, i + 1, r)
        
        return 2 * self._score(S, l + 1, r - 1)