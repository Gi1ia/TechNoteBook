class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s): 
            return s
        
        res = [""] * numRows # Each element is a row in zigzag conversation
        index, step = 0, 1
        
        for x in s:
            res[index] += x
            
            if index == 0: # If we reached the first row, go positive
                step = 1
            elif index == numRows - 1: # If we reached the last row, go negative
                step = -1
            
            index += step
        
        return "".join(res)