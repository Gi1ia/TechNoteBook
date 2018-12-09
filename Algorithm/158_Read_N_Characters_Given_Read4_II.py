"""
    The API: int read4(char *buf) reads 4 characters at a time from a file.

    The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

    By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

    Note:
    The read function may be called multiple times.

    Example 1: 

    Given buf = "abc"
    read("abc", 1) // returns "a"
    read("abc", 2); // returns "bc"
    read("abc", 1); // returns ""
    Example 2: 

    Given buf = "abc"
    read("abc", 4) // returns "abc"
    read("abc", 1); // returns ""

    #FB #G #Uber #String
"""
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.deque = collections.deque()

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        
        # Call once: 
        # Assume you are always going to read from the start of the file/bufer.
        # Call multiple times: 
        # Start reading from where you left off. 
        # This means that you have to store the last place (ptr) where you 
        # stopped and store the read but uncopied bytes to the buffer.
        i = 0

        while i < n:
            buf4 = [''] * 4
            current = read4(buf4)
            self.deque.extend(buf4)
            count = min(len(self.deque), n - i)
            if not count:
                break # EOF

            buf[i:] =[self.deque.popleft() for _ in range(count)]
            i += count
        
        return i
