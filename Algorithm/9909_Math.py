"""
If a number is odd, the next transform is 3*n+1
If a number is even, the next transform is n/2
The number is finally transformed into 1.
The step is how many transforms needed for a number turned into 1.
Given an integer n, output the max steps of transform number in [1, n] into 1.
"""
class Transform():
    def __init__(self):
        self.seen = {}
        self.seen[0] = 0
        self.seen[1] = 0

    def find_most_transform(self, n):
        if not n:
            return 0

        res = 0
        for i in range(1, n + 1):
            current = self.transform_one(i)
            # print(current)
            res = max(res, current)
        
        return res

    def transform_one(self, n):
        if n in self.seen:
            return self.seen[n]

        if n % 2 == 0:
            res = 1 + self.transform_one(n//2)
        else:
            res =  1 + self.transform_one(3 * n + 1)
        self.seen[n] = res
        return res

obj = Transform()
n = 3
print(obj.find_most_transform(19)) # Expect 20
print(obj.find_most_transform(1)) # Expect 0
print(obj.find_most_transform(12)) # Expect 19
