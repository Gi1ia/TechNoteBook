class misc():

	def shortest_path(self, board, start, end):
		"""
		:type board: List[List[int]]
		:type start: tuple(int, int)
		:type end: tuple(int, int)
		:return: list[tuple(int, int)]
		Note: In board, board[i][j] == 1 means blocked; board[i][j] == 0 means free to go.
		"""
		# TODO: validate input

		res = []
		check_list = [start]
		path = [[ [] for x in range(len(board(0)))] for y in range(len(board))]

		while check_list:
			current = check_list.popleft()
			x, y = current[0], current[1]
			if not self.is_valid(x, y, board):
				continue
			
			# Since we look for path by using BFS, 
			# we block the points that we've already visited.
			board[x][y] = 1
			path[x][y].append(current)
			if current == end:
				return path[x][y]
			check_list.extend[(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
		
		return []

	def is_valid(self, x, y, board):
		if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == 1:
			return False
		return True 