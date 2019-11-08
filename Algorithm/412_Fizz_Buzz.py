class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        
        for num in range(1, n + 1):
            divisible_by_3 = (num % 3 == 0)
            divisible_by_5 = (num % 5 == 0)
            
            res_string = ""
            
            if divisible_by_3:
                res_string += 'Fizz'
            if divisible_by_5:
                res_string += 'Buzz'
            if not res_string:
                res_string = str(num)
            
            res.append(res_string)
        
        return res