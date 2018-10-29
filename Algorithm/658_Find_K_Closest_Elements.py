class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # It can solved with binary search with 2 pointers too.


    def findClosestElements_sort(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if not arr:
            return []

        arr.sort(key = lambda _: abs(_-x)) # sort based on abs() value
        
        res = arr[:k]
        res.sort()
        return res
