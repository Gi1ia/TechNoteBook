class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # Idea: Pop 2 items from heap, if first char can be append, then append 1st
        # other wise append 2nd
        # edge case: check if heap is None before pop 2nd element
        # O(NlogN)?

        if not S:
            return ""
        
        char_count = collections.defaultdict(int)
        for char in S:
            char_count[char] += 1
        
        h = []
        for k in char_count:
            heapq.heappush(h, (-char_count[k], k))
        
        res = []
        i = 0
        while h:
            count1, char1= heapq.heappop(h)
            if h:
                count2, char2 = heapq.heappop(h)
            else:
                count2, char2 = 0, ""
            if res == []:
                res.append(char1)
                if count1 + 1 < 0:
                    heapq.heappush(h, (count1 + 1, char1))
                if char2 != "":
                    heapq.heappush(h, (count2, char2)) 
            else:
                if char1 != res[i]:
                    res.append(char1)
                    if count1 + 1 < 0:
                        heapq.heappush(h, (count1 + 1, char1))
                    if char2 != "":
                        heapq.heappush(h, (count2, char2))
                elif char2 != "":
                    res.append(char2)
                    if count2 + 1 < 0:
                        heapq.heappush(h, (count2 + 1, char2))
                    heapq.heappush(h, (count1, char1))
                else:
                    return ""            
                i += 1
        
        return "".join(res)
                
