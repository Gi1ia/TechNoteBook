# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        dummy = NestedInteger()
        q = deque()
        q.append(dummy)
        i = 0
        
        while (i < len(s)):
            if s[i] == "[": 
                n = NestedInteger()
                q[-1].add(n) # Add a nested list into the NestedInteger
                q.append(n) # Add the nested list into the stack, so we can add int into it.
                i += 1
            elif s[i] == "]":
                q.pop() # A nested list is completed. Pop it from stack.
                i += 1
            elif s[i] == ",":
                i += 1
            else:
                j = i
                while (j < len(s)) and ('0' <= s[j] <= '9' or s[j] == '-'): # We move j to see what the integer is
                    j += 1
                q[-1].add(int(s[i:j]))
                i = j
                
        return q[0].getList()[0] #?
                
        