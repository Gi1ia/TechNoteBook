import collections
import string

class Solution():
    def ladder_length(self, beginWord, endWord, wordList):
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict.discard(beginWord)
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front 
                                for index in range(len(beginWord)) for ch in 'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                # there are common elements in front and back, done
                return length
            length += 1
            if len(front) > len(back):
                # swap front and back for better performance (fewer choices in generating nextSet)
                front, back = back, front
            # remove transformations from wordDict to avoid cycle
            wordDict -= front
        return 0

    def ladderLength_basic_BFS(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # TODO: valid input
        word_set = set(wordList)
        word_set.discard(beginWord)
        dist = 0

        to_visit = collections.deque()
        to_visit.append(beginWord)

        while to_visit:
            dist += 1
            ladder = collections.deque()
            for word in to_visit:
                if word == endWord:
                    return dist
                self.add_next_word_group(word, ladder, word_set)
            to_visit = ladder    

        return 0

    def add_next_word_group(self, oldword, ladder, word_set):
        word_set.discard(oldword)
        for i in range(len(oldword)):
            for j in string.ascii_lowercase:
                new_word = oldword[:i] + j + oldword[i + 1:]
                if new_word in word_set:
                    ladder.append(new_word)
                    # word_set.discard(oldword)
                
s = Solution()
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"
wordList2 = ["hot","dot","dog","lot","log"]
wordList3 = ["hot","dot","dog","lot","log","cog", "coa", "zoa", "zoo"]
print(s.ladderLength_basic_BFS(beginWord, endWord, wordList))