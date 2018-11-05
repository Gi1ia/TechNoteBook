from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)

class FileSystem():
    def __init__(self):
        self.store = TrieNode()

    def set_path(self, path):
        node = self.store
        insert = filter(None, path.split("/"))
        if len(insert) > 1:
            if not self.start_with(insert[:-1]):
                raise ValueError('oops!')
        
        for c in insert:
            node = node.children[c]
        
    
    def get_path(self, path):
        """
        Get depth
        """
        check = filter(None, path.split('/'))
        if not self.start_with(check):
            raise ValueError('oops')

        count = 0   
        node = self.store
        for c in check:
            count += 1
            node = node.children[c]
        
        print(count)
        return count
    
    def start_with(self, prefix):
        node = self.store
        for letter in prefix:
            if letter not in node.children:
                return False 
            node = node.children[letter]
        
        return True



explorer = FileSystem()
explorer.set_path("/a")
explorer.set_path("/a/b")
explorer.get_path("/a/b")
explorer.set_path('/c/d')
explorer.set_path('/c')
