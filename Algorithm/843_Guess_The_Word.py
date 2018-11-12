# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        # This is not a solution will get accepted every time
        # For a better approach, see post:
        # https://leetcode.com/problems/guess-the-word/discuss/133862/Random-Guess-and-Minimax-Guess-with-Comparison

        n = 0
        while n < 6: # wrong answer
            attempt = random.choice(wordlist)
            n = master.guess(attempt)
            
            # shrink word list so that we only test same match of the guess
            wordlist = [w for w in wordlist if self.match_cnt(attempt, w) == n]
        
    
    def match_cnt(self, word1, word2):
        match = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                match += 1
        
        return match