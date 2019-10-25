class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars or len(chars) <= 1:
            return len(chars)
        
        left, right = 0, 0
        while right < len(chars):
            current, repeat = chars[right], 0
            while right < len(chars) and current == chars[right]:
                repeat += 1
                right += 1
            chars[left] = current
            left = left + 1
            
            #Only compress if repeat > 1
            if repeat > 1:
                
                # in case repeat is > 9, we have more number digits
                for c in str(repeat):
                    chars[left], left = c, left + 1
                
        return left