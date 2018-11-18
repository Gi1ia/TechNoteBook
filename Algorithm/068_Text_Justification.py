"""
    Given an array of words and a width maxWidth, 
    format the text such that each line has exactly 
    maxWidth characters and is fully (left and right) justified.
"""

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            # len(cur) is the same of num of spaces
            if len(cur) + num_of_letters + len(w) > maxWidth:
                # assign spaces
                for i in range(maxWidth - num_of_letters):
                    # give each words extra space after itself
                    cur[i%(len(cur) - 1 or 1)] += " "  # `or 1` is to deal with len(cur) == 1
                    
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            
            # if we can still add w into cur
            cur += [w]
            num_of_letters += len(w)
        
        return res + [' '.join(cur).ljust(maxWidth)] # left justify the last row
        