"""
So in summary, if k = 1, we can just basically rotate the array unless we get to the smallest lexicographical order. If K >= 2, we can simply exchange the relative order of any pair of elements in the string. First, we rotate the array appropriately, until we manage to have the desired pair at the beginning of the array. Then we can swap the relative order of the pair by just applying 2-move. That's why we can just sort the String for the case k >= 2.
"""

import collections

class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S:
            return ""

        if K == 1:
            return min(S[:i] + S[i:] for i in range(len(S)))
        
        return "".join(sorted(S))


s1, k1 = "acbd", 2 #abcd
s2, k2 = "acbfegd", 3 # abcdefg
s = Solution()
print(s.orderlyQueue(s2, k2))