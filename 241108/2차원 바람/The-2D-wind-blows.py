directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def rotBoard(board, start, end):
	tmpBoard = [[cell for cell in row] for row in board]
	
	for j in range(start[1] + 1, end[1]):
		board[start[0]][j] = tmpBoard[start[0]][j - 1] # UpperRow
	board[start[0]][start[1]] = tmpBoard[start[0] + 1][start[1]]
	for j in range(start[1], end[1] - 1):
		board[end[0] - 1][j] = tmpBoard[end[0] - 1][j + 1] # LowerRow
	board[end[0] - 1][end[1] - 1] = tmpBoard[end[0] - 1][end[1] - 1]
	for i in range(start[0] + 1, end[0] - 1):
		board[i][start[1]] = tmpBoard[i + 1][start[1]]
		board[i][end[1] - 1] = tmpBoard[i - 1][end[1] - 1]
	
	return board
	

def meanBoard(board, N, M, start, end):
	tmpBoard = [[cell for cell in row] for row in board]
	for i in range(start[0], end[0]):
		for j in range(start[1], end[1]):
			cnt = 1
			s = tmpBoard[i][j]
			for d in directions:
				if 0 <= i + d[0] < N and 0 <= j + d[1] < M:
					s += tmpBoard[i + d[0]][j + d[1]]
					cnt += 1
			board[i][j] = s // cnt
			
	return board


def main():
	N, M, Q = map(int, input().split())
	board = [[0] * M for _ in range(N)]
	for i in range(N):
		board[i] = list(map(int, input().split()))
		
	for i in range(Q):
		r1, c1, r2, c2 = map(int, input().split())
		start, end = [r1 - 1, c1 - 1], [r2, c2]
		board = rotBoard(board, start, end)
		board = meanBoard(board, N, M, start, end)

	for row in board:
		print(*row)
		

if __name__ == "__main__":
	main()