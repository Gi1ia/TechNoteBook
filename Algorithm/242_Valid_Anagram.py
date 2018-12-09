class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # O(1) space because len(count) < 26
        count = collections.defaultdict(int) 
        
        for c in s:
            count[c] += 1
        
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        
        for key, val in count.items():
            if val > 0:
                return False
        
        return True