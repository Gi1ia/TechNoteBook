def min_human(tasks, days):
    """
    type days: int
    type task: List[int]
    """
    
    N = len(tasks)
    memo = [[0 for _ in range(N)] for _ in range(days)]

    