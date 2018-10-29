class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        N = len(nums)
        dp = [[0 for _ in range(N + 1)] for _ in range(m + 1)]
    



    def min_human(self, tasks, days):
        """
        type days: int
        type task: List[int]
        """    
        N = len(tasks)
        memo = [[0 for _ in range(N)] for _ in range(days)]
        
        # Could be improve? the initial status?
        cumlative = [0 for _ in range(N+1)]
        for i in range(N):
            cumlative[i + 1] = cumlative[i] + tasks[i]
        
        print("cumlative", cumlative)
        
        memo[0] = cumlative[1:]

        for i in range(days):
            memo[i][0] = tasks[0]

        # The following code should be able to be clean
        for i in range(1, days):
            for j in range(1, N):
                if j <= i:
                    res = max(memo[i][j - 1], tasks[j])
                else:
                    res = float('inf')
                    for x in range(j):
                        today = cumlative[j + 1] - cumlative[x + 1] # how many tasks we do at day[j]
                        current = max(today, memo[i - 1][x]) # people that current plan need
                        res = min(res, current) # min of all plan
                memo[i][j] = res   # write to dp space
        
        for row in memo:
            print(row)

        return memo[-1][-1]