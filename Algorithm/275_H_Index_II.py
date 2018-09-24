class Solution:
    def hIndex_template2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        total = len(citations)
        count = 0

        # Template 2
        # left == right
        # left/ right could be illegal
        left, right = 0, total
        while left < right:
            mid = left + (right - left) // 2
            count = total - mid
            if citations[mid] < count:
                left = mid + 1
            else:
                right = mid
        
        if left == len(citations):
            return 0
        elif citations[left] >= total - left:
            return total - left
        else:
            return 0
        
    
    def hIndex_template3(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        total = len(citations)
        count = 0

        # Template 3
        # left + 1 == right
        # Both left and right will be legal
        left, right = 0, total - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            count = total - mid
            if citations[mid] < count:
                left = mid
            else:
                right = mid
        
        # We are looking for fisrt citation number >= count
        # thus, left has higher priority then right index.
        if citations[left] >= total - left:
            return total - left
        elif citations[right] >= total - right:
            return total - right
        else:
            return 0
        

            
        
        
            