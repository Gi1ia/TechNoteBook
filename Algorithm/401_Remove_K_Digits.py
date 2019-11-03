"""For string nums, remove k digits from it and make it minimum number possible.
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []
        
        # Construct a monotone increasing sequence of digits
        for digit in num:
            # compare digit with nums in stack.
            # There is nothing to do with nums now.
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
            
            numStack.append(digit)
            
        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack
        
        # trip the leading zeros or return "0" for empty string
        return "".join(finalStack).lstrip('0') or "0"