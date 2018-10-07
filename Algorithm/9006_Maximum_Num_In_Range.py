def max_stones(stones, camera):
    #TODO: validate input
    
    left, right = 0, 0
    res = [0, 0]
    for left in range(len(stones)):
        if right < len(stones):
            new_stone = stones[right]
        else:
            new_stone = stones[right % len(stones)] + 360
               
        while new_stone - stones[left] <= camera:

            if right - left + 1 > res[0]:
                res[0] = right - left + 1
                res[1] = stones[left]
            right += 1

            if right < len(stones):
                new_stone = stones[right]
            else:
                new_stone = stones[right % len(stones)] + 360

    
    return res[1]

stones = [10, 20, 80, 120, 170, 360]
stones2 = [10, 10, 10]
stones3 = [10, 130, 240, 350]
camera = 100
print(max_stones(stones3, camera))