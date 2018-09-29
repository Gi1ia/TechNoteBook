# ref: https://fizzbuzzed.com/top-interview-questions-5/
# https://leetcode.com/problems/palindrome-pairs/discuss/79195/O(n-*-k2)-java-solution-with-Trie-structure

class Trie_Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_dict = Trie()
        for i, word in enumerate(words):
            word_dict.addWord(word, i)
                
        res = []
        for i, word in enumerate(words):
            potential = self.get_palindrome(word, i, word_dict)
            res.extend([i, suffix] for suffix in potential if suffix != i)
        
        return res
    
    def get_palindrome(self, word, index, trie):
        res = []
        node = trie.root
        while word:
            if node.end >= 0: # one suffix ends here. e.g. for word "abcde", we found "cba".
                if self.is_palindrome(word): # Note: Also need to check word itself
                    res.append(node.end)
            if word[0] not in node.children:
                return res
            node = node.children[word[0]]
            word = word[1:]
        
        if node.end >= 0: # pair "abc" & "cba"
            res.append(node.end)
            
        res.extend(node.palindrome_below) # pair "abc" and "ffcba"/"fcba"
        
        return res  
    
    def is_palindrome(self, s):
        return s == s[::-1]
        

class TrieNode():
    def __init__(self):
        # key: letter
        # value: trieNode which has children == {}
        self.children = collections.defaultdict(TrieNode)
        self.palindrome_below = [] # index of string that begin with palindrome
        self.end = -1 # word ends here

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word, index):
        node = self.root
        reversed_word = reversed(word)
        for i, letter in enumerate(reversed_word):
            if self.is_palindrome(word[:len(word) - i]):
                node.palindrome_below.append(index)
            node = node.children[letter]
        node.end = index
    
    def is_palindrome(self, s):
        return s == s[::-1]
        
        



class Hashmap_Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        d = {}
        res = []
        for i, word in enumerate(words):
            d[word] = i
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                
                # prefix != "" ==> pair like ("abc", "cba") can be added only once
                # d[suffix[::-1] ] != i (current index), make sure that sigle palindrome won't be added as pair. e.g. ("s", "s")
                if prefix == prefix[::-1] and suffix[::-1] in d \
                and d[suffix[::-1]] != i and prefix != "":
                    temp = []
                    temp.append(d[suffix[::-1]])
                    temp.append(i)
                    res.append(temp)
                
                # ["a", "b", "ab"]
                if suffix == suffix[::-1] and prefix[::-1] in d \
                and d[prefix[::-1]] != i:
                    temp = []
                    temp.append(i)
                    temp.append(d[prefix[::-1]])
                    res.append(temp)
        
        return res