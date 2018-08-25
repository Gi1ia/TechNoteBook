class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        
        res = [True for x in range(n)]
        res[0] = False
        res[1] = False
        
        for i in range(2, n):
            if res[i] == True:
                # ((n - 1) // i) + 1 to make sure that we can reach the end of n
                for j in range(2, (n - 1)//i + 1):
                    res[i * j] = False
        
        return sum(res)