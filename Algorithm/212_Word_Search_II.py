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
            result.appedn(path)
            node.is_word = False # ??

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