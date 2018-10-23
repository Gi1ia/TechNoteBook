import collections

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        
        # flip all 1 before i, thus Ones == 0
        # or flip all 0 after i
        # Since i start from 0
        Ones = 0
        Zeros = collections.Counter(S)["0"]
        
        if Zeros == 0 or Zeros == len(S):
            return 0
        
        res = Zeros # Assume we need to flip all 0 to 1
        
        for i in range(len(S)):
            if S[i] == '1':
                Ones += 1
            else:
                Zeros -= 1
            
            res = min(res, Zeros + Ones)

        
        return res