import collections

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        BFS, stop at every possible split.
        """       
        if not wordDict:
            return False
        
        word_set = set(wordDict)
        queue = collections.deque()
        visited = [False for _ in range(len(s))]
        
        queue.append(0)
        while queue:
            start = queue.popleft()
            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in word_set:
                        queue.append(end)
                        if end == len(s):
                            return True
                        
                visited[start] = True
            
        return False
            
                
        