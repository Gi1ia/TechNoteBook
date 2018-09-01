"""
Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
    
    def mark_redundant(self, s):
        """
        return :List[int], index of right parenthesis that need to be removed
        """
        stack = []
        counter = 0
        for i in range(len(s)):
            if s[i] == "(":
                counter += 1
            elif s[i] == ")":
                counter -= 1
                if counter < 0:
                    stack.append(i)
                    counter = 0
            else:
                continue
        
        return stack
    
    def remove(self, s, stack):
        
    
    def is_valid(self, s):
        """
        :return: bool
        """
        counter = 0
        for char in s:
            if char == "(":
                counter += 1
            elif char == ")":
                counter -= 1
                if counter < 0:
                    return False
            else:
                continue

        return counter == 0