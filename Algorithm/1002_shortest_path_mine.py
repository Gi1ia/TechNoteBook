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
		# TODO: validate input

		check_list = collections.deque()
		path = [start]
		check_list.append(path)
		height, width = len(board), len(board[0])
		visited = [[False for x in range(width)] for y in range(height)]
		visited[start[0]][start[1]]=True

		dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

		while check_list:
			current_path = check_list.popleft()
			current_point = current_path[-1]
			x, y = current_point[0], current_point[1]

			for drct in dirs:
				j = drct[0] + x
				k = drct[1] + y

				if (j >= 0 and k >= 0 and j < height and k < width and \
				visited[j][k] == False and board[j][k] == 0):
					new_path = current_path[:]
					new_path.append((j, k))

					if j == end[0] and k == end[1]:
						return new_path
								
					visited[j][k] = True
					check_list.append(new_path)
		
		return []

s = misc()
board = [[0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
board_no_ans = [[0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [0, 0, 0, 1]]
start = (0, 2)
end = (3, 0)

print(s.shortest_path_II(board, start, end))