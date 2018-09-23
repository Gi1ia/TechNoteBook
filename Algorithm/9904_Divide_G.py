"""
5/3 = 1.66666
"""
class Solution():
    def divide(self, divdent, divisor):
        """ divdent/divisor
        divdent: int
        divisor: int
        return: tuple(string, string)
        """
        if not divisor: # illegal
            return None 

        have_seen = dict()
        loop = []             
        quotient = divdent // divisor
        remainder = divdent % divisor
        
        # Early return
        if remainder == 0:
            return (str(quotient))       
       
        position = 1
        loop.append(quotient)
        while remainder not in have_seen:           
            # loop.append(quotient)      
            divdent = remainder * 10
            quotient = divdent // divisor
            have_seen[remainder] = position
            loop.append(quotient)
            position += 1 # Currently, no value at loop[position]
            remainder = divdent % divisor
        
        loop_range = len(loop) - have_seen[remainder]
        
        return str(loop[0]) + "." + ''.join(str(_) for _ in loop[1:]) + "range" + str(loop_range)

s = Solution()
# print(s.divide(50, 7))
print(s.divide(5, 6))
        

            


