"""
Given an integer array A, and an integer target, return the number of tuples i, j, k
such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Note:
3 <= A.length <= 3000
0 <= A[i] <= 100
0 <= target <= 300
"""

class Solution:
    def threeSumMulti_TLE(self, A, target):
        """
        :type A: List[int]
        :type target: int
        :rtype: int
        """
        A.sort()
        N = len(A)
        res = 0
        mod = 1000000007
        
        for i in range(N - 2):
            l, r = i + 1, N - 1
            cnt = 0
            while l < r:
                if A[l] + A[r] + A[i] < target:
                    l += 1
                elif A[l] + A[r] + A[i] > target:
                    r -= 1
                else:
                    if A[l] != A[r]:
                        cnt_l, cnt_r = 1, 1
                        while l + 1 < r and A[l + 1] == A[l]:
                            cnt_l += 1
                            l += 1
                        while r - 1 > l and A[r - 1] == A[r]:
                            cnt_r += 1
                            r -= 1
                        cnt += (cnt_l * cnt_r) % mod
                        l += 1
                        r -= 1
                    else:
                        n = r - l + 1 # how many choices do we have
                        cnt += ((n * (n - 1))//2)%mod # we choose 2 from choices
                        break # increase i; don't edit l or r
            res += cnt
            res %= mod
        
        return res



