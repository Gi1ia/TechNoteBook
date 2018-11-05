class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        start = self.ip_to_int(ip)
        res = []
        while n:
            # if n is smaller than biggest block we can take,
            # we can't use the biggest block.
            capacity = min(n, start & -start)
            
            # generate the greediest block
            mask = 32 - (capacity.bit_length() - 1)
            
            res.append(self.int_to_ip(start) + '/' + str(mask))
            
            start += 1 << (32 - mask) # end of mask has been consumed. start from a new position
            n -= 1 << (32 - mask) # continue to fill rest of n
        
        return res
    
    def ip_to_int(self, ip):
        res = 0
        for x in ip.split('.'):
            res = res * 256 + int(x)
        return res
    
    def int_to_ip(self, num):
        return ".".join(str((num >> i) % 256) for i in (24, 16, 8, 0))
        