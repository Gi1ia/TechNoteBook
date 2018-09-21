import collections

class SuperStack():
    def __init__(self):
        self.stack = collections.deque()
        self.increase = collections.defaultdict(int)
    
    def Push(self, v):
        self.stack.append(v)
    
    def Pop(self):
        if not self.stack:
            return 
        cursor = len(self.stack) - 1
        res = self.stack.pop()
        if cursor in self.increase:
            res += self.increase[cursor]
            del self.increase[cursor]

        return res

    def Inc(self, bottom, diff):
        bottom = min(len(self.stack), bottom)
        if bottom <= 0:
            return
        
        for i in range(bottom):
            self.increase[i] += diff

s = SuperStack()
print(s.stack, s.increase)
s.Push(1)
print(s.stack, s.increase)
s.Push(2)
print(s.stack, s.increase)
s.Inc(3, 1)
print(s.stack, s.increase)
s.Pop()
print(s.stack, s.increase)