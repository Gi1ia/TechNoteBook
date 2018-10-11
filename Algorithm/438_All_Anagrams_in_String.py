class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        start, end = 0, 0
        
        # Counter(p) is very slow
        
        maps = {} # we want it to be zero while iterate s
        for c in p:
            maps[c] = maps.get(c, 0) + 1
        
        counter = len(maps) # formed characters
        
        while end < len(s):
            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] == 0:
                    counter -= 1
            
            end += 1 # end point to next of validated char already.
            while counter == 0: # not all s[start:end] is anagrams now
                if end - start == len(p):
                    res.append(start)
                if s[start] in maps:
                    maps[s[start]] += 1 
                    if maps[s[start]] == 1: # we only change counter the first time we lose a character.
                        counter += 1
                start += 1
        
        return res
                        