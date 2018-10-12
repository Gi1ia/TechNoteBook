class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache():
    def __init__(self, capacity):
        self.size = capacity
        self.dict = {}
        self.last = Node(0, 0)
        self.head = Node(0, 0)
        self.last.prev = self.head
        self.head.next = self.last
    
    def get(self, key):
        if key not in self.dict:
            return -1
        
        # get the node
        n = self.dict[key]
        # remove key from dict and linked list
        self._remove(n)
        # Add it back so it could on the top
        self._add(n)

        return n.value
    
    def put(self, key, value):
        if key in self.dict:
            n = self.dict[key]
            self._remove(n)
        
        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.size:
            first = self.head.next
            self._remove(first)
            del self.dict[first.key]
    
    def _remove(self, node):
        p = node.prev
        q = node.next
        p.next = q
        q.prev = p
    
    def _add(self, node):
        p = self.last.prev
        p.next = node
        node.prev = p
        node.next = self.last
        self.last.prev = node


# Concurrency:
# 1. Lock the entire access, then edit hash map and linked list
# 2. Use two different locks for linked list and hash map
#    --> read hash --> del hash item --> del lru item --> read lru item
# 3. Use multiple LRU linked list 

# Ref: LFU https://www.kunxi.org/blog/2016/12/lfu-cache-in-python/
