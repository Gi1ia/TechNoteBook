class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == None or len(digits) == 0:
            return []

        keyboard = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                    '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        all_Combinations = [] # result to store all combinations

        # Get current(Nth) digit
        for digit in digits:
            current = list()

            # Get corresponding letter for the digit (3/4 possibilities)
            for letter in keyboard[digit]:

                # Get previous combination (lenth should be N-1 )
                for combination in all_Combinations:

                    # Append the current letter to previouse combination. Add the Nth letter.
                    current.append(combination + letter)

            # Override the final result
            all_Combinations = current
        
        return all_Combinations

    def letterCombinations_pattern(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == None or len(digits) == 0:
            return []
        
        keyboard2 = {'':'', '0':'', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
                    '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        self.helper(digits, keyboard2, '', res, 0)

        return res
    
    def helper(self, digits, pattern, path, res, pos):
        if len(path) == len(digits):
            res.append(path[:])
            return
        
        for i in range(pos, len(digits)):
            for j in range(len(pattern[digits[i]])):
                current_letter = pattern[digits[i]][j]
                path += current_letter
                self.helper(digits, pattern, path, res, i + 1)
                path = path[:-1]

s = Solution()
digits = "234"
result = s.letterCombinations(digits)
print (result)
print (s.letterCombinations_pattern(digits))
input("Press Enter")