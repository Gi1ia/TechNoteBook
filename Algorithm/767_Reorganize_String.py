import collections
import heapq

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""

        char_count = collections.defaultdict(int)
        for c in S:
            char_count[c] += 1
        
        h = []
        for key in char_count:
            heapq.heappush(h, (-char_count[key], key))

        # Early return when there is no valid solution
        if any(-count > (len(S) + 1) / 2 for count, x in h):
            return ""

        res = []
        i = 0
        while len(h) >= 2:
            count1, c1 = heapq.heappop(h)
            count2, c2 = heapq.heappop(h)
            # Since Python will also compare letter alpha beta
            # We can make sure that c1, c2 will always in order
            # So below code coulde be eliminated:
            #if not ans or ch1 != ans[-1]:
            #    ans.extend([ch1, ch2])
            #else:
            #    ans.extend([ch2, ch1])
            res.extend([c1, c2])
            if count1 + 1 < 0:
                heapq.heappush(h, (count1 + 1, c1))
            if count2 + 1 < 0:
                heapq.heappush(h, (count2 + 1, c2))
            
        return "".join(res) + (h[0][1] if h else "")

    
    def reorganizeString_naive_approach(self, S):
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
                
