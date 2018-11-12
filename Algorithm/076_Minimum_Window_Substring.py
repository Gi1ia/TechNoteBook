import collections

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        dict_t = collections.Counter(t)
        required = len(dict_t) # how many chars we need to form
        
        l, r = 0, 0
        
        # formed will +1 once we have 1. char in t; 2. number of char in s is equal to the number of char in t
        formed = 0
        window_counts = {}
        
        # res tuple of the form (window length, left, right)
        res = (float("inf"), None, None)
        
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1 # Same as the default dict
            
            # right pointer
            # NOTE: here we allow window_counts[character] > dict_t[character]
            # it's only we won't plus formed number if its '>'
            if character in dict_t and window_counts[character] == dict_t[character]:
                    formed += 1 # We've successfult build one char
                
            # Size down the window
            while l <= r and formed == required:
                character = s[l]
                
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                
                # Shrink 
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1 # lost one formed letter
                
                l += 1
            
            r += 1
            
        return "" if res[0] == float("inf") else s[res[1]:res[2] + 1]
                
            
        