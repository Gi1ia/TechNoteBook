class GuessNumber():
    def __init__(self, target):
        self.target = target

    def try_num(self):
        candidates = {1, 2, 3, 4, 5, 6}

        # First Round
        for i, v in candidates.items():
            num = [i for i in range(4)]
            temp = self.guess_server()

    
    def guess_server(self, nums):
        """
        return: List[int, int]
        """
        pass