class Solution():
    def get_ones(self, num):
        """
        type: num: int
        return: int
        Note: 
        Change num to list[int]
        If we want to calculate num[-2] (digits in ten), we need to know what is in num[-2]
        num[-2] == 1: k = num_before_num[-2] * 10 (digit in ten/factor) + num_after_num[-2](num[-1]) + 1
        e.g. 13 => 0 * 10 + 3 + 1
        num[-2] == 0: k = num_before_num[-2] * factor
        e.g. 303 => 3 * 10 
        num[-2] > 1: k = num_before_num[-2] * factor + factor
        e.g. 323 => 3 * 10 + 10
        """

        if not num:
            return 0
        
        sum = 0
        current = num
        factor = 1

        while current > 0:
            digit = current % 10
            current /= 10
            reminder = num % factor
            if digit == 0:
                sum += current * factor
            elif digit == 1:
                sum += current * factor + reminder + 1
            else:
                sum += (current + 1) * factor
            factor *= 10

        return sum
        

s = Solution()

print(100)
print(s.get_ones(100))