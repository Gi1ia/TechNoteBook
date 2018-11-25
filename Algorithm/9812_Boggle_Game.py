from collections import defaultdict

class BoggleGame:
    def find_path(self, board, words):
        if not board or not board[0]: return 0
        
        words_dict = Trie()
        for w in words:
            words_dict.insert(w)
        
        node = words_dict.root
        self.root = words_dict.root

        self.longest = 0
        self.res = ""
        for i in range(len(board)):
            for j in range(len(board[0])):
                seen = 0 
                visited = set()
                if board[i][j] in node.children:
                    visited.add((i, j))
                    self.dfs(board, i, j, "", node.children[board[i][j]], visited, seen)
        
        return self.res
    
    def dfs(self, board, x, y, path, node, visited, seen):
        path += board[x][y]

        if node.is_word:
            seen += 1
            if seen > self.longest:
                self.longest = seen
                self.res = path
            node = self.root # NOTE: Reset note to root to find other words
        
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for d in dirs:
            xx, yy = x + d[0], y + d[1]
            if xx >= 0 and yy >= 0 and xx < len(board) and yy < len(board[0])\
            and (xx, yy) not in visited and board[xx][yy] in node.children:
                visited.add((xx, yy))
                # print(board[xx][yy])
                self.dfs(board, xx, yy, path, node.children[board[xx][yy]], visited, seen)
                visited.discard((xx, yy))
        
        path = path[:-1]
        if node.is_word: # NOTE: minus seen number
            seen -= 1
        return
        

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

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","e"],["i","a","t","y"]]
words = ["oath","pea","eat","rain", "key"]


foo = BoggleGame()
print(foo.find_path(board, words))