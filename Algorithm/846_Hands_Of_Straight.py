class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if not hand:
            return False
        
        count = collections.Counter(hand)
        
        # Try to remove smallest number with len(straight) == W
        while count:
            m = min(count)
            for _ in range(W):
                if count[m] <= 0:
                    return False
                else:
                    count[m] -= 1
                    if count[m] == 0:
                        count.pop(m, None)
                m += 1
        
        return True
                
        
        