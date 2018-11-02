class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        Time O(2^n)
        Space: O(log n)? 
        """
        if not n:
            return []
        
        left, right = n, n
        res = []
        self.helper(left, right, res, "")
        
        return res
        
    
    def helper(self, left, right, res, current):
        if right < left:
            # More ) then ( 
            return 
        
        if left == right == 0:
            res.append(current[:])
            return
        
        if left > 0:
            current += '('
            self.helper(left - 1, right, res, current)
            current = current[:-1]
        
        if right > 0:
            current += ')'
            self.helper(left, right - 1, res, current)
            current = current[:-1]