class Solution:
    def maxDistToClosest2(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        prev = -1
        res = float('-inf')
        if seat[0] == 1:
            prev = 0

        for i, seat in enumerate(seats):
            if i == 1:
                if prev == -1:
                    res = max(res, i)
                else:
                    res = max(res, (i - prev) // 2)
                prev = i
        
        if seat[-1] == 0:
            res = max(res, len(seats) -1 - prev)
            
        return res

    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if not seats:
            return None
        
        if len(seats) == 1:
            return 0 if seats[0] == 0 else None
        
        seats.insert(0, float('-inf'))
        seats.append(float('inf')) # length of seats become n + 2
        prev = 0
        max_dist = -1
        
        for current, seat in enumerate(seats):
            if seat == 1:
                dist = (current - prev)//2 if prev != 0 else current - 1 # -1 because we insert inf at index 0
                if dist > max_dist:
                    max_dist = max(max_dist, dist)
                prev = current
            elif seat == float('inf'):
                dist = current - prev - 1 # -1 because we append inf to the end
                if dist > max_dist:
                    max_dist = max(max_dist, dist)           
        
        return max_dist 

seats = [1,0,0,0]
seats2 = [1, 1]
s = Solution()
print(s.maxDistToClosest(seats2))