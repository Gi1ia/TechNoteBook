from heapq import heappush, heappop, heapify
import unittest

class RoundPrice():
    def round_II(self, nums, target):
        if not nums:
            return 0
        
        modify = []
        res = []
        gross = 0
        for i in range(len(nums)):
            r = int(nums[i])
            res.append(r)
            gross += r
            diff = abs(nums[i] - r)
            heappush(modify, (-diff, i))
        
        should_fix = abs(target - gross)

        for j in range(should_fix):
            current = heappop(modify)
            res[current[1]] += 1
        
        return res

    def round(self, nums, target):
        if not nums:
            return 0
        
        modify = []
        gross = 0
        res = []
        fix = set()
        # trim = 0
        for i, num in enumerate(nums):
            num_int = int(num)
            gross += num_int
            diff = abs(num - num_int)
            # trim += diff
            heappush(modify, (-diff, i))
        
        should_fix = abs(target - gross)

        for j in range(should_fix):
            current = heappop(modify)
            fix.add(current[1])
        
        for i, num in enumerate(nums):
            if i in fix:
                # trim -= abs(int(num) - num)
                # trim += abs(int(num) + 1 - num)
                res.append(int(num) + 1)
            else:
                res.append(int(num))

        # print(trim)
        return res

class TestRoundPrice(unittest.TestCase):
    def test_round_II(self):
        priceRounder = RoundPrice()
        origin = [5.6, 5.6, 5.6, 1.2, 3.3]
        target = 21
        expected1 = [6, 6, 5, 1, 3]
        self.assertEqual(expected1, priceRounder.round_II(origin, target))

if __name__ == '__main__':
    unittest.main()

origin = [5.6, 5.6, 5.6, 1.2, 3.3]
target = 21
obj = RoundPrice()
print(obj.round_II(origin, target))