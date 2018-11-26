import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False

class FileSystem():
    def __init__(self):
        self.root = TrieNode()
    
    def create(self, path):
        to_add = filter(None, path.split("/"))
        if len(to_add) > 1:
            exist = self._find(to_add[:-1])
            if not exist:
                # raise ValueError("Path Error")
                print("Path error")
                return

        self._insert(to_add)
        
        print(path, " created")

    def get(self, path):
        to_check = filter(None, path.split("/"))
        exist = self._find(to_check)
        print(" Found ")
        return exist

    def _insert(self, path):
        node = self.root
        for c in path:
            node = node.children[c]
        node.end = True
    
    def _find(self, path):
        node = self.root
        for c in path:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return node.end
    
    def _last(self, path):
        node = self.root
        for c in path:
            node = node.children[c]
        
        return node


explorer = FileSystem()
explorer.create("/a")
# explorer.watch("/a")
explorer.create("/a/b")
explorer.get("/a/b")
explorer.create('/c/d')
explorer.create('/c')
