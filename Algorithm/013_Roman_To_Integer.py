class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        prev = 0
        
        read = {"I": 1, "V": 5, "X":10, "L":50, "C": 100, "D": 500, "M": 1000}
        
        for c in range(len(s) - 1, -1, -1):
            num = read[s[c]]
            if num < prev:
                total -= num
            else:
                total += num
            prev = num
        
        return total
            
        