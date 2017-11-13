def minMoves(piece, start, end):
	# type: (str, tup, tup) -> int

	if start[0] > 7 or start[0] < 0 or start[1] > 7 or start[1] < 0 \
		or end[0] > 7 or end[0] < 0 or end[1] > 7 or end[1] < 0:
		return -1
	if start[0] == end[0] and start[1] == end[1]:
		return 0
	if piece == 'KING':
		# Shortest path for king will always be the 'diagonal'
		return abs(end[0] - start[0]) + abs(end[1]-start[1])
	elif piece == 'BISHOP':
		# We can define a simple function to see if the bishop is on the correct diagonal
		def sameColorSpace(start,end):
			return ((start[0] + start[1]) % 2) == ((end[0] + end[1]) % 2)
		if sameColorSpace(start,end):
			if abs(end[0] - start[0]) == abs(end[1]-start[1]):
				# Start and end lie on the same diagonal
				return 1
			else:
				# Start and end don't lie on the same diagonal. Minimum moves is always 2 in this case
				return 2
		else:
			return -1
	elif piece == 'KNIGHT':
		# Adjacency List
		grid = [[0 for _ in range(8)] for _ in range(8)]
		# Queue for BFS containing current position and num moves
		queue = [(start, 0)]
		def getMoves(pos):
			possible_moves = [(-1,-2),(-2,-1),(1,-2),(-1,2),(1,2),(2,1),(2,-1),(-2,1)]
			legal_moves = []
			for moves in possible_moves:
				row = pos[0][0] + moves[0]
				col = pos[0][1] + moves[1]
				if row >= 0 and row < 8 and col >= 0 and col < 8:
					if grid[row][col] == 0:
						legal_moves.append(((row,col), pos[1] + 1))
			return legal_moves
		while len(queue) > 0:
			pos = queue.pop()
			grid[pos[0][0]][pos[0][1]] = 1
			moves = getMoves(pos)
			if pos[0] == end:
				# BFS finds shortest path
				return pos[1]
			for move in moves:
				queue.insert(0,move)
	return -1 

if __name__ == "__main__":
	#test
	print(minMoves('KING', (0,0), (7,7)))
	print(minMoves('BISHOP', (0,0), (2,2)))
	print(minMoves('KNIGHT', (0,0), (4,5)))
