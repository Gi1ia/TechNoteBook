from collections import defaultdict

class BoggleGame:
    def find_path(self, board, words):
        if not board or not board[0]: return 0
        
        

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True