class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ""
        
        LCP = None
        for s in strs:
            if LCP == None:
                LCP = s
            else:
                # NOTE: Make sure to enumerate LCP here instead of s
                for i, e in enumerate(LCP):
                    if i >= len(s) or e != s[i]:
                        LCP = s[:i]
                        break
                        
        return LCP
        
    def longestCommonPrefix_I(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or not strs[0]:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        LCP = strs[0]
        for i in range(1, len(strs)):
            count = 0
            for j in range(min(len(strs[i]), len(LCP))):
                if strs[i][j] == LCP[j]:
                    count += 1
                    continue
                else:
                    break
            if count <= len(LCP):
                LCP = strs[i][:count]
        
        return LCP