import collections
import string

class Solution():
    def ladder_length(self, beginWord, endWord, wordDict):
        length = 2
        front, back = set([beginWord]), set([endWord])
        wordDict = set(wordDict)
        wordDict.discard(beginWord)

        # We need to remove edge case if we proceed changing from both side
        if endWord not in wordDict:
            return 0
        
        # Only check the smaller size word set(front), because we don't merge back and wordDict
        while front:
            # generate all valid transformations
            front = wordDict & (set(word[:index] + ch + word[index+1:] for word in front\
                                for index in range(len(beginWord)) for ch in string.ascii_lowercase))
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

    def ladderLength_basic_BFS_TLE(self, beginWord, endWord, wordList):
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

        to_visit = set()
        to_visit.add(beginWord)

        while to_visit:
            dist += 1
            ladder = set()
            for word in to_visit:
                if word == endWord:
                    return dist
                ladder = self.add_next_word_group(word, ladder, word_set)
            to_visit = ladder    

        return 0

    def add_next_word_group(self, oldword, ladder, word_set):
        word_set.discard(oldword)
        ladder = set(oldword[:index] + char + oldword[index + 1:] for index in range(len(oldword)) for char in string.ascii_lowercase) & word_set
        print(ladder)

        return ladder
        """
        for i in range(len(oldword)):
            for j in string.ascii_lowercase:
                new_word = oldword[:i] + j + oldword[i + 1:]
                if new_word in word_set:
                    ladder.append(new_word)
        """
                
s = Solution()
wordList = ["hot","dot","dog","lot","log","cog"]
beginWord = "hit"
endWord = "cog"
wordList2 = ["hot","dot","dog","lot","log"]
wordList3 = ["hot","dot","dog","lot","log","cog", "coa", "zoa", "zoo"]

long_start = "sand"
long_end = "acne"

print(s.ladderLength_basic_BFS_TLE(beginWord, endWord, wordList))