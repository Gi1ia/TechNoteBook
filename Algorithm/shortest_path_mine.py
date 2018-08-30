class misc():
	def shortest_path(self, board, start, end):
		# TODO: validate input

		check_list = [start]
		board[start[0]][start[1]] = 1
		path = [[ [] for x in range(len(board(0)))] for y in range(len(board))]

		while check_list:
			current = check_list.popleft()
			if not is_valid(current):
				path
