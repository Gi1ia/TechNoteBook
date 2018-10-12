# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0

        res = float("-inf")
        N = len(points)

        if N < 2:
            return N

        for p1 in range(N - 1):
            maps = {}
            same = 0
            temp = 0
            for p2 in range(p1 + 1, N):
                if self.same_points(points[p1], points[p2]):
                    same += 1
                else:
                    slope = self.find_slope(points[p1], points[p2])
                    maps[slope] = maps.get(slope, 0) + 1
            
            for i, j in maps.items():
                if j > temp:
                    temp = j
            
            res = max(res, temp + same  + 1) # Add the first point back to result 
        
        return res

        
    def find_slope(self, p1, p2):
        """
        :return type: float
        """
        diff_y = p1.y - p2.y
        diff_x = p1.x - p2.x       
        if diff_x == 0:
            return float("inf")
        
        gcd = self.gcd(diff_y, diff_x)

        return (diff_y / gcd, diff_x / gcd)
    
    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)
    
    def same_points(self, p1, p2):
        return p1.x == p2.x and p1.y == p2.y


points = [[0,0],[94911151,94911150],[94911152,94911151]]
s = Solution()
print(s.maxPoints(points))