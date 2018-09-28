class Solution:
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
                if suffix == suffix[::-1] and prefix[::-1] in d \
                and d[prefix[::-1]] != i:
                    temp = []
                    temp.append(i)
                    temp.append(d[prefix[::-1]])
                    res.append(temp)
        
        return res