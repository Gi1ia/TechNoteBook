from collections import deque, defaultdict
from heapq import heappush, heappop, heapify

class Wizard():
    def shortest(self, wizards):
        """
        wizards: List[List[int]]
        """
        visited = set()
        check = []
        heappush(check, (0, 0, wizards[0])) # distance, wizard_id, wizard_neighbors

        distance = {}
        for i in range(1, 10):
            distance[i] = float('inf')

        distance[0] = 0

        while check:
            dis, current, neighbors = heappop(check)
            
            print("current: ", current)
            print("dis: ", distance)

            # find the 10th wizard
            if current == 9:
                return distance[current]

            curr_dis = distance[current]
            for neighbor in neighbors:
                e = (neighbor - current) ** 2
                if curr_dis + e < distance[neighbor]:
                    distance[neighbor] = curr_dis + e
                heappush(check, (distance[neighbor], neighbor, wizards[neighbor]))

obj = Wizard()
wizards = [[1, 2], [3], [3, 4], [4], [5, 6, 7], [8], [7], [8, 9], [9], [9]]
wizards2 = [[1, 5, 9], [2, 3, 9], [4], [], [], [9], [], [], [], []]
print(obj.shortest(wizards2))

        
        
        
