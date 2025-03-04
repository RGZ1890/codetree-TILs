def zfil(board):
	for i in range(4):
		for j in range(3, 0, -1):
			if board[i][j - 1] == 0:
				board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
	
	return board


def comb(board):
	for i in range(4):
		ref = 0
		for j in range(1, 4):
			if board[i][j] == 0:
				break
			if board[i][j] == board[i][j - 1]:
				board[i][j - 1], board[i][j] = 2 * board[i][j - 1], 0
	board = zfil(board)
	
	return board


def move(board, d):
	if d == 'R':
		board = [[cell for cell in row[::-1]] for row in board]
	elif d == 'U':
		board = [[board[i][j] for i in range(4)] for j in range(4)]
	elif d == 'D':
		board = [[board[i][j] for i in range(3, -1, -1)] for j in range(4)]
		
	board = zfil(board)
	
	board = comb(board)
	
	if d == 'R':
		board = [[cell for cell in row[::-1]] for row in board]
	elif d == 'U':
		board = [[board[i][j] for i in range(4)] for j in range(4)]
	elif d == 'D':
		board = [[board[i][j] for i in range(4)] for j in range(3, -1, -1)]
	
	return board


def main():
	board = [[0] * 4 for _ in range(4)]
	for i in range(4):
		board[i] = list(map(int, input().split()))
	d = input()
	board = move(board, d)
	for row in board:
		print(*row)
	

if __name__ == "__main__":
	main()