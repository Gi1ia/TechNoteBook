"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary_recursive(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) == 0:
            return b
        
        if len(b) == 0:
            return a
        
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary_recursive(self.addBinary_recursive(a[0:-1], b[0:-1], '1')) + '0'
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary_recursive(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary_recursive(a[0:-1], b[0:-1]) + '1'

    def addBinary_by_bits(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        
        a = list(a)[::-1]
        b = list(b)[::-1]
        sum = 0
        res = ""

        for i in range(len(a)):
            sum += int(a[i])
            sum += int(b[i]) if i < len(b) else 0
            res += str(sum % 2) # get modulus, add it to result 
            sum = sum // 2 # floor division sum for carry

        if sum:
            res += str(sum)

        return res[::-1]