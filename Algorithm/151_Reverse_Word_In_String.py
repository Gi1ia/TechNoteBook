class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l, r = 0, len(s) - 1
        
        d, word = collections.deque(), []
        while l <= r:
            if s[l] == ' ' and word:
                d.appendleft(''.join(word))
                word = []
            elif s[l] != ' ':
                word.append(s[l])
            l += 1
            
        # append the last word
        d.appendleft(''.join(word))
        
        return ' '.join(d)