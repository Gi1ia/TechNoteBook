class Solution():
    def daily_temperature_stack(self, temperatures):
        if not temperatures:
            return []
        if len(temperatures) < 2:
            return [0]
        
        res = [0 for x in range(len(temperatures))]
        stack = [] # we want to store tuple (temp, index) in to stack

        for i in range(len(temperatures)):
            while len(stack) > 0:
                if temperatures[i] <= stack[-1][0]:
                    break
                else:
                    res[i] = i - stack[-1][1]
                    stack.pop()
            stack.append((temperatures[i], i))
        
        return res


s = Solution()
input = [73,74,75,71,69,72,76,73]
print(s.daily_temperature_stack(input))


                