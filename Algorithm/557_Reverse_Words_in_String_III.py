class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        wordList = s.split(" ")
        reverse = []
        for word in wordList:
            reverse.append(word[::-1])
            
        result = " ".join(reverse)
        
        return result