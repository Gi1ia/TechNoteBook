import collections

class misc():
	def shortest_path_II(self, board, start, end):
		"""
		:type board: List[List[int]]
		:type start: tuple(int, int)
		:type end: tuple(int, int)
		:return: list[tuple(int, int)]
		Note: In board, board[i][j] == 1 means blocked; board[i][j] == 0 means free to go.
		"""
		check_list = collections.deque()
		path = [start]
		check_list.append(path)
		height, width = len(board), len(board[0])
		visited = [[False for x in range(width)] for y in range(height)]

		while check_list:
			current_path = check_list.popleft()
			current_point = current_path[-1]
			x, y = current_point[0], current_point[1]

			if (x < 0 or y < 0 or x >= height or y >= width or visited[x][y] == True or board[x][y] == 1):
				continue
			if x == end[0] and y == end[1]:
				return current_path
			
			visited[x][y] = True
			path1 = current_path[:]
			path1.append((x - 1, y))
			
			path2 = current_path[:]
			path2.append((x + 1, y))
			
			path3 = current_path[:]
			path3.append((x, y - 1))
			
			path4 = current_path[:]
			path4.append((x, y + 1))
			check_list.extend([path1, path2, path3, path4])
		
		return []


	def shortest_path(self, board, start, end):
		"""
		:type board: List[List[int]]
		:type start: tuple(int, int)
		:type end: tuple(int, int)
		:return: list[tuple(int, int)]
		Note: In board, board[i][j] == 1 means blocked; board[i][j] == 0 means free to go.
		"""
		# TODO: validate input

		check_list = collections.deque()
		check_list.append(start)
		path = []
		res = []

		while check_list:
			current = check_list.popleft()
			self.find_next(current, end, board, path, res, check_list)
		
		return res

	def find_next(self, current, end, board, path, res, check_list):
		x, y = current[0], current[1]
		if x < 0 or y < 0 or x >= len(board)\
		 or y >= len(board[0]) or board[x][y] == 1:
			return
		
		path.append[current]
		if current == end:
			res.append(path[:])

		# I'm confused here:
		# Since we are looking for path by using BFS, 
		# we should block the points that we've already visited?
		board[x][y] = 1
		check_list.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])
		board[x][y] = 0
		
		return