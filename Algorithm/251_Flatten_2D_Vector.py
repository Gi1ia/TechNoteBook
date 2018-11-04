class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.store = vec2d[::-1]

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext:
            return self.store.pop()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.store:
            return False
        
        while len(self.store) > 0:           
            top = self.store.pop()
            
            if isinstance(top, int):
                self.store.append(top)
                return True
            
            if len(top) == 0:
                continue
        
            temp = []
            for i in range(len(top) - 1, -1, -1):
                temp.append(top[i])

            self.store.extend(temp)
            return True
            
        return False
            
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())