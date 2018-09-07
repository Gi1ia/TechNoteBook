class Solution:
    def __init__(self):
        self.count = 0
        
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N:
            return 0
        used = [False for _ in range(N + 1)]

        # TLE
        # self.find_TLE(N, [], used)
        self.find(N, 1, used)

        return self.count
    
    def find(self, N, position, used):
        """ We don't need to memorize entire path, record the count only"""
        if position == N:
            self.count += 1
            return
        
        for i in range(1, N + 1):
            if used[i]:
                continue
            if not self.divisible(position + 1, i):
                continue
            used[i] = True
            self.find(N, position + 1, used)
            used[i] = False
        
    def find_TLE(self, N, path, used):
        if len(path) == N:
            self.count += 1
            return
        
        for i in range(1, N + 1):
            if used[i]:
                continue
            if not self.divisible(len(path) + 1, i):
                continue
            used[i] = True
            path.append(i)
            self.find_TLE(N, path, used)
            used[i] = False
            path.pop()
    
    def divisible(self, index, num):
        if index % num == 0 or num % index == 0:
            return True
        return False

s = Solution()
print(s.countArrangement(5))