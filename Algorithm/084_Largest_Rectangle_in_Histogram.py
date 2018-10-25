class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        heights.append(0) # make sure the heights will have a drop
        res = 0
        
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                
                # Below code is not correct, because we need to pop the height before calculating the width.
                '''
                h = heights[stack[-1]]
                w = i - stack[-1] 
                stack.pop()
                '''
                res = max(res, h * w)
            stack.append(i)
        
        heights.pop() # Edit origin data back.
        return res