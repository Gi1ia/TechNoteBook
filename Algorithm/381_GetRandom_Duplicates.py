import collections
import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.position = collections.defaultdict(set)
        self.store = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        pos = len(self.store)
        self.store.append(val)
        self.position[val].add(pos)
        
        return len(self.position[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not self.position[val] or not self.store:
            return False

        idx = self.position[val].pop()
        replace = self.store[-1]     
        self.store[idx] = replace
        self.position[replace].add(idx) # Note: Add first, then discard.... 
        self.position[replace].discard(len(self.store) - 1)    
        self.store.pop(-1)
        
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.store:
            return -1
        
        l = len(self.store)
        idx = random.randrange(l)
        return self.store[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()