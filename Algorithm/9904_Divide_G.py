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
        res = []             
        quotient = divdent // divisor
        remainder = divdent % divisor
        
        # Early return
        if remainder == 0:
            return (str(quotient))       
       
        position = 1
        res.append(quotient) # Append result before decimal point
        while remainder not in have_seen:           
            # res.append(quotient)      
            divdent = remainder * 10
            quotient = divdent // divisor
            have_seen[remainder] = position
            res.append(quotient)
            position += 1 # Currently, no value at res[position]
            remainder = divdent % divisor
        
        loop_range = len(res) - have_seen[remainder]
        
        return str(res[0]) + "." + ''.join(str(_) for _ in res[1:]) + " loop " + str(loop_range) + " digit"

s = Solution()
print(s.divide(200, 97))
print(s.divide(1, 6))
        

            


