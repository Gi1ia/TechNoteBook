class Arrange():
    def split(self, players):

        """
        This solution is not pretty right.
        Assign has to be 2*n size. But it's good for dynamic input.
        players: [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (3, 0), (3, 1), (4, 1)]
        """
        if not players:
            return
        players.sort(key = lambda x: x[0])
        N = len(players) if len(players) % 2 == 0 else len(players) + 1
        print(N)
        assign = [0 for _ in range(2 * N)]
        
        for player in players:
            i = 1
            assign[i] = 1 if assign[i] == 0 else 0
            while i < N:
                i = 2 * i + assign[i]

                assign[i] = 1 if assign[i] == 0 else 0
            assign[i] = player
            print(assign[N:])
        
        return assign[N:]
    
    def split_odd_even(self, players):
        """
        split odd and even then recursive
        """
        pass
        # TODO

foo = Arrange()
test1 = [(1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]
print(foo.split(test1))
