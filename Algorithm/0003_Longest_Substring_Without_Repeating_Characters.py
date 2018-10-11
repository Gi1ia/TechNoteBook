import collections

class TwoPointerSolution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {}
        start, end = 0, 0
        counter = 0
        res = 0
        
        while end < len(s):
            char = s[end]
            
            maps[char] = maps.get(char, 0) + 1
            if maps[char] > 1:
                counter += 1
            
            end += 1
            
            while counter > 0: # we have duplicated char
                temp = s[start]
                if temp in maps and maps[temp] > 1:
                    counter -= 1
                maps[temp] -= 1 # even if maps[temp] == 1, we still need to decrease the counter
                start += 1
            
            res = max(res, end - start)
        
        return res

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        max_len = 0
        start = 0
        repeat_char = {}
        
        for i in range(len(s)):
            if s[i] in repeat_char:
                # Looking for last location of repeated char (s[i])
                # and compare with other repeated char location
                # e.g. "abba"
                start = max(repeat_char[s[i]], start)
            # @start start from 0, so we need +1 to get the real length.
            max_len = max(max_len, i - start + 1)
            # exclude the repeated char's index
            repeat_char[s[i]] = i + 1
        
        return max_len
            

s = Solution()
s1 = "abcabcbb"
s2 = "dvdf"
s3 = "abba"
print(s.lengthOfLongestSubstring(s3))