from heapq import heappush, heappop, heapify

class RoundPrice():

    def round(self, nums, target):
        if not nums:
            return 0
        
        modify = []
        gross = 0
        res = []
        fix = set()
        trim = 0
        for i, num in enumerate(nums):
            num_int = int(num)
            gross += num_int
            diff = abs(num - num_int)
            trim += diff
            heappush(modify, (-diff, i))
        
        should_fix = abs(target - gross)

        for j in range(should_fix):
            current = heappop(modify)
            fix.add(current[1])
        
        for i, num in enumerate(nums):
            if i in fix:
                trim -= abs(int(num) - num)
                trim += abs(int(num) + 1 - num)
                res.append(int(num) + 1)
            else:
                res.append(int(num))

        print(trim)
        return res

origin = [5.6, 5.6, 5.6, 1.2, 3.3]
target = 21
obj = RoundPrice()
print(obj.round(origin, target))