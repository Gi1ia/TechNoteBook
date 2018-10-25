class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return "0"
        
        s =s.replace(" ", "")
        stack = []
        num = 0
        operator = "+"
        
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            
            # we are actually locating the second number in a formula
            # so we use a variable to store the previous
            if s[i] in "*+-/" or i == len(s) - 1:
                if operator == "+":
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack.append(stack.pop() * num)
                else:
                    top = stack.pop()
                    current = int(top/num)
                    stack.append(current)
                    
                    # for python 2
                    """
                    tmp = stack.pop()
                    if tmp//num < 0 and tmp%num != 0:
                        stack.append(tmp//num+1)
                    else:
                        stack.append(tmp//num)
                    """
                
                # clear num and operator
                num = 0
                operator = s[i]
        
        return sum(stack) # add all num in stack
                
                