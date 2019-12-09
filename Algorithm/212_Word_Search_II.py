import collections

class Trie_Tree_Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]: return []
        
        words_dict = Trie()
        for w in words:
            words_dict.insert(w)
        
        node = words_dict.root
        
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if board[i][j] in node.children:
                    visited.add((i, j))
                    self.dfs(board, i, j, "", res, node.children[board[i][j]], visited)
        
        return res
    
    def dfs(self, board, x, y, path, res, node, visited):
        path += board[x][y]
        
        if node.is_word:
            res.append(path)
            node.is_word = False
        
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for d in dirs:
            xx, yy = x + d[0], y + d[1]
            if xx >= 0 and yy >= 0 and xx < len(board) and yy < len(board[0])\
            and (xx, yy) not in visited and board[xx][yy] in node.children:
                visited.add((xx, yy))
                # print(xx, yy, path, res, node)
                self.dfs(board, xx, yy, path, res, node.children[board[xx][yy]], visited)
                visited.discard((xx, yy))
        
        path = path[:-1]
        return

class Word_Game():
    def find_words(self, board, words):
        if not board or not board[0]:
            return []

        visited = [[0 for y in range(len(board[0]))] for x in range(len(board))]
        result = []
        
        # Convert the words list into a trie tree
        word_dic = Trie()
        node = word_dic.root
        for w in words:
            word_dic.insert(w)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.exist(board, i, j, node, visited, "", result)

        return result


    def exist(self, board, x, y, node, visited, path, result):
        """
        return type: void
        """
        if node.is_word:
            result.append(path)
            node.is_word = False # Mark as false to de-dup

        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or visited[x][y] == 1:
            return
        
        current_node = node.children.get(board[x][y])
        if not current_node:
            return 
        
        # the letter in the trie tree, add it into potential word path
        path += board[x][y]
        visited[x][y] = 1
        self.exist(board, x - 1, y, current_node, visited, path, result)
        self.exist(board, x + 1, y, current_node, visited, path, result)
        self.exist(board, x, y - 1, current_node, visited, path, result)
        self.exist(board, x, y + 1, current_node, visited, path, result)
        visited[x][y] = 0
        
        return


class Trie_Node():
    def __init__(self):
        self.children = collections.defaultdict(Trie_Node)
        self.is_word = False
    
class Trie():
    def __init__(self):
        self.root = Trie_Node()

    def insert(self, word):
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.is_word = True

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

# Test case 2
board2 = [["a","a"]]
words2 = ["aaa"]
foo = Solution()
foo.findWords(board, words)