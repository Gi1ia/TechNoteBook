class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        # Bell-man Ford solution
        # Bell-man Ford is a solution for single source, multiple dst with K steps
        # For mutiple source, see floyd algorithm
        dp = [[float('inf') for _ in range(n)] for _ in range(K + 2)] 
        dp[0][src] = 0 # NOTE: remember to initialize start
        
        # f[k][v] = min(f[k][v], f[k-i][u] + f[i][v]) for i in range(1, k)
        for i in range(1, K + 2):
            dp[i][src] = 0 # from src to src is always 0
            for city1, city2, fee in flights:
                dp[i][city2] = min(dp[i][city2], dp[i - 1][city1] + fee)
        
        print(dp)
        # NOTE: check the dst coordinate instead of last(-1) element in dp
        return -1 if dp[-1][dst] == float('inf') else dp[-1][dst]

# Test 1
n = 2
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 1
dst = 0
K = 0
obj = Solution()
print(obj.findCheapestPrice(n, flights, src, dst, K))