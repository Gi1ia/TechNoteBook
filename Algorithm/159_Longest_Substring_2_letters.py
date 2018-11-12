class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = collections.defaultdict(int)
        cnt = 0
        start, end = 0, 0
        res = float("-inf")
        
        while end < len(s):
            c = s[end]
            seen[c] += 1
            if seen[c] == 1:
                cnt += 1            
            end += 1
            
            while start <= end and cnt > 2:
                temp = s[start]
                seen[temp] -= 1
                if seen[temp] == 0:
                    cnt -= 1
                start += 1 
            
            res = max(res, end - start)
        
        return res if res != float("-inf") else 0
        
        