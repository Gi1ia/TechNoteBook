class Solution:
    def shortestPalindrome_TLE(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        cursor = 0
        for i in range(len(s)):
            if self.is_palindrome(s, 0, i):
                cursor = max(cursor, i) #s[:cursor + 1] should be palindrome
        
        add = s[cursor + 1:]
        add = add[::-1]
        
        return add + s 
    
    def is_palindrome(self, s, l, r):
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        
        if l - 1 == r or l == r:
            return True
        
        return False
        