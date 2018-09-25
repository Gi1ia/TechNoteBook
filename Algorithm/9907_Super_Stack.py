import collections

class SuperStack():
    def __init__(self):
        self.stack = collections.deque()
        self.increase = collections.defaultdict(int)
    
    def Push(self, v):
        self.stack.append(v)
    
    def Pop(self):
        if not self.stack:
            return None
        cursor = len(self.stack) - 1
        res = self.stack.pop()
        if cursor in self.increase:
            diff = self.increase[cursor]
            res += diff
            del self.increase[cursor]
            self.increase[cursor - 1] += diff

        return res

    def Inc(self, bottom, diff):
        bottom = min(len(self.stack), bottom)
        if bottom <= 0:
            return
        
        self.increase[bottom - 1] += diff

s = SuperStack()
print(s.stack, s.increase)
s.Push(1)
print(s.stack, s.increase)
s.Push(2)
print(s.stack, s.increase)
s.Inc(3, 1)
print(s.stack, s.increase)
print("pop " + str(s.Pop()))
print(s.stack, s.increase)
print("pop " + str(s.Pop()))