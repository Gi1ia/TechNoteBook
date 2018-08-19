"""
Give a `List` of data representing the coordinates[x, y] of each restaurant. 
Customer's coordinates are at the origin [0, 0]
Find out the `n` restaurants closest to the customer, return their coordinates in the original order.

Example:
n = 2
List = [[0, 0], [1, 1], [2, 2], [3, 3]]

return:
[[0, 0], [1, 1]]

"""
import heapq
class Solution():
    def Closest_Restaurants_II(self, n, restaurants):
        """
        :type restaurants: List[List[int]]
        :type n: int
        :return: List[List[int]]
        """
        if restaurants == None or len(restaurants) < 2:
            return [[]]
        
        if len(restaurants) < n:
            return restaurants
        
        res = []

        for i in range(n):
            dis = self.Calculate_Distance(restaurants[i])
            if len(res) < k or - dis > res[0][0]:
                if len(res) == k:
                    heapq.heappop(res)
                heapq.heappush(res, (-dis, restaurant[i]))

        return [x for x in res[1]]

    
    def Calculate_Distance(self, coord):
        """
        :type coord: List[int]
        :return: float
        """

        # TODO: handle pow over flow
        res = sqrt(pow(coord[0], 2) + pow(coord[1], 2))

        return res