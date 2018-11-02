def longest(nums):
    if not nums:
        return 1

    res = 1
    current = 1
    has_break = False
    prev = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1] and nums[i] > prev:
            current += 1
            res = max(res, current)
            prev = nums[i]
        else:
            if not has_break:
                has_break = True
                current += 1
                res = max(res, current)
                prev = nums[i - 1]
            else:
                has_break = False
                current = 1
                prev = nums[i]
        
    return res

test = [3, 1, 4, 5, 2, 7, 9]
print(longest(test))

