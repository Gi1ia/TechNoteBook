class Art_Word():
    def __init__(self, price, quality):
        self.min_price = x
        self.quality_point = quality
    
class Solution():
    def buy_N_arts_heap(self, arts):
        

    def Get_All_Arts(self, arts):
        """
        arts: List[Art_work]
        return: float; price to buy all art
        """
        # TODO: valid input
        if not arts:
            return 0
        
        ratio = float('-inf')
        sum_points = 0
        res = 0
        for art in arts:
            price = art.min_price
            quality = art.quality_point
            ratio = max(ratio, price/quality)
            sum_points += quality

        # TODO: handle overflow
        try:
            res = sum_points * ratio
        catch ex:
        # TODO
        # pass

        return res
    
    def Get_N_Arts(self, arts, N):
        possible = self.Find_N_Arts(arts, N)

        res = float('inf')
        for single_set in possible:
            value = self.Get_All_Arts(possible)
            res = min(value, res)
        
        return res

    def Find_N_Arts(self, arts, N):
        """
        return: List[List[Art_Word]]
        """
        # TODO: valid input
        
        res = []
        self.dfs(arts, 0, [], N, res)
        return res

    def dfs(self, arts, pos, current, N, res):
        """
        return: float; price to buy N arts
        """
        if len(current) == N:
            #res.append(current[:])
            # res.append()
            return
        
        for i in range(pos, len(arts)):
            # if len(arts) - i < N: return
            # caculate single art
            current.append(arts[i])
            self.dfs(arts, pos + 1, current, N, res)  
            current.pop(arts[i])


        




[(20, 1), (14, 2), (30, 1), (40, 4), (100, 100)]
# 1. lower price is better
# 2. R of lower won't incease other arts
# N = 3
# r == 30



arts = [(20, 1), (14, 2), (30, 1)]
# 1: r == 20; sum_points = 1
# 2: temp_r = 7; r == 20; sum_points = 3
# 3: temp_r = 30; r == 30; sum_points = 4
# res: 120
arts2 = [(20, 3), (50, 2), (50, 3)]
# 1: r == 20/3, sum_points = 3
# 2: t_r == 25, r == 25