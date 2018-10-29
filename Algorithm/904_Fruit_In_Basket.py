class Solution:
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        count = collections.defaultdict(int)
        unique = 0
        start, end = 0, 0
        res = 0
        
        while end < len(tree):
            count[tree[end]] += 1
            if count[tree[end]] == 1:
                unique += 1
            while unique > 2:
                count[tree[start]] -= 1
                
                # First, see if we successfully remove a kind of tree
                if count[tree[start]] == 0:
                    unique -= 1
                
                # Second, move the pointer. Other wise it will out of range
                start += 1
            
            res = max(res, end - start + 1)
            end += 1
        
        return res
                
        