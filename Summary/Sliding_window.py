"""
    #  problems:
    # 003 ./Algorithm/003_Longest_Substring_Without_Repeating_Characters.py
    # 076 ./Algorithm/076_Minimum_Window_Substring.py 
    # https://leetcode.com/problems/substring-with-concatenation-of-all-words/
    # https://leetcode.com/problems/find-all-anagrams-in-a-string/
    # 159. https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

    # Ref: https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/discuss/49708/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.
"""

class Template:
    def sliding_window_template(self, s, t):
        res = []

        target = collections.Counter(t)
        cnt = len(target) # how many rules/forms we need to meet

        begin, end = 0, 0

        # find in source string
        while end < len(s):
            c = s[end]
            if c in target:
                target[c] -= 1 # could be negative
                if target[c] == 0:
                    cnt -= 1
            end += 1

            while start <= end and cnt == 0:
                # could get answer here
                length = end - start

                temp = s[start]
                if temp in target:
                    target[temp] += 1
                    if target[temp] > 0:
                        cnt += 1

                start += 1
        
        return 