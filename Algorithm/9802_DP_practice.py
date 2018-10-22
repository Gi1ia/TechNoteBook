"""
    1D problem 2D DP solution. (implied 3D)
"""

def min_human_need_debug(tasks, days):
    """
    type days: int
    type task: List[int]
    """    
    N = len(tasks)
    memo = [[0 for _ in range(N + 1)] for _ in range(days + 1)]
    
    cumlative = [0 for _ in range(N + 1)]
    for i in range(N):
        cumlative[i + 1] = cumlative[i] + tasks[i]
    print("cumlative", cumlative)
    
    memo[1] = cumlative

    # day[i] map to memo[i + 1]
    # task[j] map to 
    for i in range(1, days):
        for j in range(N):            
            res = float('inf')
            for x in range(j + 1): # j start from 0; we want to iterate to index j             
                today = cumlative[j + 1] - cumlative[x]
                current = max(today, memo[i][j])
                res = min(res, current)
            memo[i + 1][j + 1] = res
    
    print("memo")
    for row in memo:
        print(row)
    
    return memo[-1][-1]



tasks = [3, 4, 1, 7, 2, 5]
days = 3
min_human(tasks, days)