from heapq import heappush, heappop, heapify

# Edge case: If len(wish) == 0, need to take care of common cases

class TravelBuddy():
    def __init__(self):
        self.buddies = [] # min heap
        self.recommendation = set()
        self.my_wish = set()

    def find_buddy(self, my_wish, friends_list):
        self.my_wish = my_wish #

        for friend, friend_wish in friends_list.items():
            common = my_wish.intersection(friend_wish)
            if len(common) >= len(my_wish) // 2:
                heappush(self.buddies, (-len(common), friend, friend_wish)) # Now we have all buddies in order
            
        # heapify(self.buddies)
        return [x[1] for x in self.buddies]
        
    def recommend(self, city_size):
        for buddy in self.buddies:
            add_wish = buddy[2] - self.my_wish
            self.recommendation = self.recommendation.union(add_wish)
            if len(self.recommendation) >= city_size:
                break

        res = list(self.recommendation)       
        return res[:city_size]
            
obj = TravelBuddy()
my_wish = {1, 3, 5, 7, 9}
friends_list = {1 : {3, 4, 5, 6}, 2 : {1, 2, 3}, 3 : {3, 4, 5, 6, 7, 10, 11, 12}}
print(obj.find_buddy(my_wish, friends_list))
print(obj.recommend(5))
