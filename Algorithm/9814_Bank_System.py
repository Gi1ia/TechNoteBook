from collections import defaultdict

class Bank():
    def __init__(self):
        self.customer = defaultdict(float)
        self.history = defaultdict(list)
    
    def deposite(self, id, timestamp, amount):
        self.customer[id] += amount
        self.history[id].append((timestamp, amount))
    
    def withdraw(self, id, timestamp, amount):
        current = self.check(id)
        if current - amount < 1e-3:
            raise exception
        
        self.customer[id] -= amount
        self.history[id].append((timestamp, -amount))

    def check(self, id):
        return self.customer[id]
    
    def print_history(self, id, start, end):
        history = self.history[id]

        left, right = 0, len(history)
        while left < right:
            mid = right - (right - left) // 2
            if history[mid] <= start:
                left = mid + 1
            else:
                right = mid
        
        if left == len(history): return []
        
        res = []
        for i in range(left, len(history)):
            if history[i][0] <= end:
                res.append
        
        return res
        