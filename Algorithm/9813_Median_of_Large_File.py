"""
Find the median from a large file of integers. You can not access the numbers by index, can only access it sequentially. 
And the numbers cannot fit in memory.
"""
import sys
# Credit: Dandan

class FindMedian:
    def find_median(self, integer_file):
        upper_bound = -float('inf')
        lower_bound = float('inf')
        total_count = 0

        with open(integer_file) as f:
            for line in f:
                value = int(line)
                upper_bound = max(upper_bound, value)
                lower_bound = min(lower_bound, value)
                total_count += 1
        if total_count == 0:
            raise Exception
    
        def search(integer_file, left, right, k):
            if left >= right:
                return left
            
            guess = left + (right - left) // 2
            max_in_left_half = left
            count = 0
            with open(integer_file) as f:
                for line in f:
                    value = int(line)
                    if value <= guess:
                        count += 1
                        max_in_left_half = max(max_in_left_half, value)
            
            # split 
            if count == k:
                return max_in_left_half
            if count < k:
                return search(integer_file, max(max_in_left_half + 1, guess), right, k)
            return search(integer_file, left, max_in_left_half, k)
        
        if total_count % 2 == 1:
            return search(integer_file, lower_bound, upper_bound, (total_count + 1)//2)
        else: 
            return (search(integer_file, lower_bound, upper_bound, total_count / 2) \
                + search(integer_file, lower_bound, upper_bound, total_count / 2 + 1)) / 2.0
