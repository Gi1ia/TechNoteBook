import collections
import heapq

class AutocompleteSystem(object):
    """
    This implementation doesn't fit request because I ues heap to shrink the result to 3
    And by default, the heap will keep sentences with large ascII result.
    Add a customize comparator to reconstruct the result to pass the OJ.
    """

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        # TODO: validate input
        self.new_sentence = []
        self.store = TrieTree()
        for i in range(len(times)):
            self.store.insert(sentences[i], times[i])

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self._update()
            # important! Clear the current sentence after we receive a end mark
            self.new_sentence = []
            return []

        suggest = []
        self.new_sentence.append(c)
        attempt = "".join(self.new_sentence)
        suggest = self.store.search(attempt)
        
        print(suggest)
        return suggest
                
    def _update(self):
        print(self.new_sentence)
        new_data = "".join(self.new_sentence)
        self.store.insert(new_data, 1)
        

class TrieTree():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sentence, plus):
        cursor = self.root
        for c in sentence:
            cursor = cursor.children[c]

        cursor.end = True
        cursor.frequency += plus
        cursor.suggest = sentence
    
    def search(self, attempt):
        cursor = self.root
        res = []
        
        for c in attempt:
            if c not in cursor.children:
                return []
            else:
                cursor = cursor.children[c]

        q = [cursor]
        while q:
            next_level = []
            for check in q:
                if check.end == True:
                    res.append((-check.frequency, check.suggest))
                    """
                    heapq.heappush(res, (check.frequency, check.suggest))
                    if len(res) > 3:
                            heapq.heappop(res)
                    """
                for c, node in check.children.items():
                    next_level.append(node)
            q = next_level
        
        res.sort(key = lambda x: (x[0], x[1]))
        res = res[:3]
        
        return [val[1] for val in res]

        
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.end = False
        self.frequency = 0
        self.suggest = None


sentences = ["i love you", "island", "ironman", "i love l"]
times = [5, 3, 2, 2]
# Your AutocompleteSystem object will be instantiated and called as such:
obj = AutocompleteSystem(sentences, times)
param_1 = obj.input("i")
param_2 = obj.input(" ")
param_3 = obj.input("a")
param_4 = obj.input("#")
param_5 = obj.input("i")
param_6 = obj.input(" ")