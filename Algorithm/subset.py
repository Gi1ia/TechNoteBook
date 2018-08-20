class Solution():
    def subset_I(self, input_nums):
        """
        """
        l = len(input_nums)

        # generate a l-length bit
        # Example l == 3
        # generate from 000 -> 111 replace 1 with input char
