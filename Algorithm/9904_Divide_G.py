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

        have_seen = dict{}
        first, second = [], []

        step = 0
        quotient = divdent // divisor
        remainder = divdent % divisor
        first.append(str(quotient))
        
        # Early return
        if remainder == 0:
            return (str(quotient), "")       

        

        while remainder not in have_seen:
            have_seen[remainder] = step
            second.append(quotient)
            second += 1
            divdent = remainder * 10
            quotient = divdent // divisor
            remainder = divdent % divisor
        

            


