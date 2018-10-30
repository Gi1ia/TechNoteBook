class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #  `num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]` 
        if num1 == '0' or num2 == '0':
            return '0'
        
        res = [0 for _ in range(len(num1) + len(num2))]
        
        # We need to ran from right to left
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])              
                p1 = i + j 
                p2 = i + j + 1
                # to see if we need to change the digit at ten's place
                temp = mul + res[p2]

                res[p2] = temp % 10
                res[p1] += temp // 10
        
        output = "".join(map(str, res))
        output = output.lstrip("0")

        return output




        