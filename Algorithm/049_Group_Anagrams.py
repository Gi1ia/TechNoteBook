"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs == None or len(strs) == 0:
            return [[]]

        keys = {}

        for single_str in strs:
            str_in_order = ''.join(sorted(single_str))
            if str_in_order in keys:
                keys[str_in_order].append(single_str)
            else:
                keys[str_in_order] = [single_str]
        
        return [keys[x] for x in keys]

    