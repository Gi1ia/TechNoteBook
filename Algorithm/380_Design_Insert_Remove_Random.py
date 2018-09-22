class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.my_set = []
        self.position = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.position:
            return False
        
        self.position[val] = len(self.my_set)
        self.my_set.append(val)
        return True
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.position:
            return False
        
        l = len(self.my_set)
        index = self.position[val]
        replace = self.my_set[-1]
        self.my_set[index] = replace
        self.position[replace] = index
        del self.position[val]
        del self.my_set[-1]
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.my_set:
            return -1
        l = len(self.my_set)
        index = random.randrange(l)
        return self.my_set[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()