class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        
        res = ""
        
        for i in range(len(s)):
            # Even number
            temp_even = self.generate_longest(i, i + 1, s)
            if len(temp_even) > len(res):
                res = temp_even
            
            temp_odd = self.generate_longest(i, i, s)
            if len(temp_odd) > len(res):
                res = temp_odd
        
        return res
        
    
    def generate_longest(self, l, r, s):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        
        return s[l + 1: r]

s = Solution()
print(s.longestPalindrome("babad"))