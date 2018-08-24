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
                res[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        
        return res
    
    def daily_temperature_array(self, temperatures):
        if not temperatures:
            return []
        if len(temperatures) < 2:
            return [0]
        
        res = [0 for x in range(len(temperatures))]

        for i in range(len(temperatures) - 1, -1, -1):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if res[j] > 0:
                    j = res[j] + j
                else:
                    j = len(temperatures) # Force j move to the end
            if j < len(temperatures):
                res[i] = j - i
            
        return res



s = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(s.daily_temperature_array(temperatures))

input("Press Enter to continue...")


                