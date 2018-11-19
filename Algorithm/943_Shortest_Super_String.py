class Solution:
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        self.length = float('inf')
        self.res = ""
        
        self.dp = [[ 0 for _ in range(len(A))] for _ in range(len(A))]
        
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j: continue
                L = min(len(A[i]), len(A[j]))
                for x in range(1, L):
                    # prefix of i is overlapped with suffix of j
                    if A[i][-x:] == A[j][:x]:
                        self.dp[i][j] = x
                        
        # print(self.dp)
        for i in range(len(A)):
            # print("new start")
            self.permutation(A[i], i, [False for _ in range(len(A))], 1, A)
        
        return self.res
        
        
    def permutation(self, path, idx, used, cnt, A):
        used[idx] = True
        # print(path, idx, used, cnt, len(A))
        if sum(used) == len(A):
            if len(path) < self.length:
                self.res = path
                self.length = len(path)
            used[idx] = False
            return
        
        # Only try the neighbors with biggest weight
        neighbors, weight = [], -1
        for j in range(len(A)):
            if not used[j] and self.dp[idx][j] > weight:
                weight = self.dp[idx][j]
                neighbors = [j]
            elif self.dp[idx][j] == weight:
                neighbors.append(j)
        
        cnt += 1
        for i in neighbors:
            if used[i]: continue
            new_l = self.dp[idx][i]
            path += A[i][new_l:]
            # print("next dfs", used[i])
            self.permutation(path, i, used, cnt, A)
            # NOTE:
            tail = len(A[i]) - new_l
            path = path[:- tail]
            # used[i] = False
                
        used[idx] = False
        cnt -= 1
                
A = ["alex","loves","leetcode"]
B = ["ymv","lpkp","ajelp","kpx"]
obj = Solution()
print(obj.shortestSuperstring(A))