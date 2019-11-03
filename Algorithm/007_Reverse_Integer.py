class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        # Python mod is not intuitive when negative
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        
        while x:
            pop = x % 10
            x = x // 10
            res = res * 10 + pop
            
        return 0 if res > pow(2, 31) else res * symbol
        
        
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = str(x)
        
        if temp[0] != '-':
            temp = temp[::-1] 
        else:
            temp2 = temp[1:]
            temp2 = temp2[::-1]
            temp = temp[0] + temp2
        # print(temp)
        
        return int(temp) if -(2**31) - 1 < int(temp) < 2**31 else 0