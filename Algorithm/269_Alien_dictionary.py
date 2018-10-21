"""
    There is a new alien language which uses the latin alphabet. 
    However, the order among letters are unknown to you. 
    You receive a list of non-empty words from the dictionary, 
    where words are sorted lexicographically by the rules of this 
    new language. Derive the order of letters in this language.

    Example 1:
    Input:
    [
    “wrt”,
    “wrf”,
    “er”,
    “ett”,
    “rftt”
    ]
    Output: “wertf”

    Example 2:
    Input:
    [
    “z”,
    “x”
    ]
    Output: “zx”

    Example 3:
    Input:
    [
    “z”,
    “x”,
    “z”
    ]
    Output: “”

    Explanation: The order is invalid, so return “”.
    Note:
    You may assume all letters are in lowercase.
    You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
    If the order is invalid, return an empty string.
    There may be multiple valid order of letters, return any one of them is fine.
"""
import collections

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        
        graph = set()
        for pair in zip(words, words[1:]): # zip will generate a list which is list of pairs
            # e.g. pair == ('wrt', 'wrf')
            # so if we unzip pair, we would get unzip = [('w', 'w'), ('r', 'r'), ('t', 'f')]
            for unzip in zip(*pair):
                a, b = unzip
                if a != b:
                    order = (a, b)
                    graph.add(order) # de-dup
                    break # letters after can not show us the sequence.
                    
        graph = list(graph)
        
        # now we have order a -> b in graph
        indegree = collections.defaultdict(int)
        outdegree = collections.defaultdict(set) # we use set to do de-dup
        
        # initial indegree
        # because later will only add from 0 to 1, will not create new entry.
        charset = set(''.join(words))
        for c in charset:
            indegree[c] = 0
        
        # build topological sort relation
        for order in graph:
            pre, post = order[0], order[1]           
            indegree[post] += 1
            outdegree[pre].add(post)
        
        res = []
        q = collections.deque()
        
        # Find all point that has indegree == 0
        for key, val in indegree.items():
            if val == 0:
                q.append(key)
                        
        while q:
            letter = q.popleft()
            res.append(letter)
            for follow in outdegree[letter]:
                indegree[follow] -= 1
                if indegree[follow] == 0:
                    q.append(follow)
        
        # if the res has the same size of the all chars, we have solution.
        # otherwise we have conflict.
        res = "".join(res) if len(res) == len(charset) else ""
        
        return res
        
            
                    