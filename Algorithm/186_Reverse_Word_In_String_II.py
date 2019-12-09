class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse_helper(s, 0, len(s) - 1)
        
        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self.reverse_helper(s, start, i - 1)
                start = i + 1
            elif i == len(s) - 1:
                self.reverse_helper(s, start, i)
            
    
    def reverse_helper(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
            