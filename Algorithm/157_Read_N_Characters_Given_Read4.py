# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        i = 0
        
        while i < n:
            buf4 = ["" for _ in range(4)]
            current = read4(buf4)
            if not current:
                break # EOF
            current = min(current, n - i)
            buf[i:] = buf4[:current] # copy to buffer
            i += current
        
        return i