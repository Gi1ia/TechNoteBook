"""For every 2K, reverse first K char.

Returns:
    [string] -- [description]
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        listFormat = list(s)
        for start in range(0, len(s), 2*k):
            i = start
            j = min(start + k - 1, len(s) - 1)
            while i < j:
                temp = listFormat[i]
                listFormat[i] = listFormat[j]
                listFormat[j] = temp
                i += 1
                j -= 1
        
        return "".join(listFormat)