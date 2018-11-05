class Solution:
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        if len(bottom) < 2:
            return False
        
        blocks = collections.defaultdict(list)
        for block in allowed:
            blocks[block[:2]].append(block[2])

        def dfs(bottom, upper):
            if len(bottom) == 1:
                return True
            
            if bottom[:2] in blocks:
                for nextElement in blocks[bottom[:2]]: # iterate all possible placement
                    if len(bottom) <= 2:
                        # move to next layer
                        # "AABA"
                        # ["AAA","AAB","ABA","ABB","BAC"]
                        if dfs(upper + nextElement, ""):
                            return True
                    else:
                        if dfs(bottom[1:], upper + nextElement):
                            return True
                    
            return False
        
        return dfs(bottom, "")
                