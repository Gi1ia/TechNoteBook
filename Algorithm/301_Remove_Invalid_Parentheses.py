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
        if not s:
            return [""]
        
        # How many left/right parentheses we need to remove
        left, right = 0, 0
        for c in s:
            if c =="(":
                left += 1
            elif c == ")":
                right = right + 1 if left == 0 else right
                left = left - 1 if left > 0 else left # Decrement count of left parentheses because we have found a right
                
        # print(left, right)
        res = set()
        def dfs(s, index, left_cnt, right_cnt, left_rem, right_rem, path):
            if index == len(s):
                if left_rem == right_rem == 0:
                    complete = "".join(path)
                    res.add(complete)
            else:
                # The discard case. Note that here we have our pruning condition.
                # We don't recurse if the remaining count for that parenthesis is == 0.
                if((s[index] == '(' and left_rem > 0) or (s[index] == ")" and right_rem > 0)):
                    # Remove current char and recursive
                    dfs(s, index + 1, left_cnt, right_cnt, left_rem - (s[index] == '('), right_rem - (s[index] == ")"), path)
                    
                # Add current char
                path.append(s[index])
                
                if s[index] not in {"(", ")"}:
                    dfs(s, index + 1, left_cnt, right_cnt, left_rem, right_rem, path)
                elif s[index] == "(":
                    dfs(s, index + 1, left_cnt + 1, right_cnt, left_rem, right_rem, path)
                elif s[index] == ")" and left_cnt > right_cnt:
                    dfs(s, index + 1, left_cnt, right_cnt + 1, left_rem, right_rem, path)
                
                path.pop()
        
        dfs(s, 0, 0, 0, left, right, [])
        
        return list(res)


class Solution_test_intuition:
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