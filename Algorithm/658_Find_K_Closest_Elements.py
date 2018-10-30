import bisect
class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        # It can solved with binary search with 2 pointers too.
        N = len(arr)
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[N - k:]
        else:
            index = bisect.bisect_left(arr, x)
            low = max(0, index - k - 1)
            high = min(N - 1, index + k - 1)

            while high - low > k - 1: # Shrink until we found k nums
                if (low < 0 or x - arr[low] <= arr[high] - x):
                    high -= 1
                elif (high > N - 1 or arr[high] - x <= x - arr[low]):
                    low += 1
                else:
                    return []
            return arr[low:high + 1]


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
