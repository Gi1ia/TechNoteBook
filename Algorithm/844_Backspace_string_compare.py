class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        This problem could also be finished with stack
        """
        
        i, j = len(S) - 1, len(T) - 1
        back_S, back_T = 0, 0
        
        while True:
            while i >= 0 and (back_S or S[i] == '#'):
                back_S += 1 if S[i] == '#' else -1
                i -= 1
            while j >= 0 and (back_T or T[j] == '#'):
                back_T += 1 if T[j] == '#' else -1
                j -= 1
            if i >= 0 and j >= 0 and S[i] == T[j]:
                i -= 1
                j -= 1
            else:
                return i == j == -1