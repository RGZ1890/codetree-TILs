directions = {'L': -1, 'R': 1, 'U': -2, 'D': 2}

def zfil(board):
	for i in range(4):
		l = len(board[i])
		board[i] = board[i] + [0] * (4 - l)
	
	return board


def comb(board):
	for i in range(4):
		ref = 0
		for j in range(1, 4):
			if board[i][j] == 0:
				break
			if board[i][j] == board[i][j - 1]:
				board[i][j - 1], board[i][j] = 2 * board[i][j - 1], 0
				
	return board


def move(board, d):
	if d == -1:
		tmpBoard = [[cell for cell in row if cell != 0] for row in board]
	elif d == 1:
		tmpBoard = [[cell for cell in row[::-1] if cell != 0] for row in board]
	elif d == -2:
		tmpBoard = [[board[i][j] for i in range(4) if board[i][j] != 0] for j in range(4)]
	else: # D
		tmpBoard = [[board[i][j] for i in range(3, -1, -1) if board[i][j] != 0] for j in range(4)]
		
	tmpBoard = zfil(tmpBoard)
	tmpBoard = comb(tmpBoard)
	
	tmpBoard = [[cell for cell in row if cell != 0] for row in tmpBoard]
	tmpBoard = zfil(tmpBoard)
	
	if d == -1:
		tmpBoard = [[cell for cell in row] for row in tmpBoard]
	elif d == 1:
		tmpBoard = [[cell for cell in row[::-1]] for row in tmpBoard]
	elif d == -2:
		tmpBoard = [[tmpBoard[i][j] for i in range(4)] for j in range(4)]
	else:
		tmpBoard = [[tmpBoard[i][j] for i in range(4)] for j in range(3, -1, -1)]
	
	return tmpBoard


def main():
	board = [[0] * 4 for _ in range(4)]
	for i in range(4):
		board[i] = list(map(int, input().split()))
	d = input()
	d = directions[d]
	board = move(board, d)
	for row in board:
		print(*row)
	

if __name__ == "__main__":
	main()