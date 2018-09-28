class Solution:
    def sho

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        cursor = 0
        for i in range(len(s), -1, -1):
            if self.is_palindrome(s[:i]:
                cursor = i
                break
        
        add = s[cursor + 1:]
        add = add[::-1]
        
        return add + s
    
    def is_palindrome(self, s):
        if s = s[::-1]:
            return True
        return

    def is_palindrome_TLE(self, s, l, r):
        while l < r and s[l] == s[r]:
            l += 1
            r -= 1
        
        if l - 1 == r or l == r:
            return True
        
        return False
        