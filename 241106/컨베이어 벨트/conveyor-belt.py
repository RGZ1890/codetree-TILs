def moveBoard(board, n):
	board = [[cell for cell in row] for row in board]
	
	tmp = board[0][n - 1]
	for i in range(n - 2, -1, -1):
		board[0][i + 1] = board[0][i]
	board[0][0] = board[1][0]
	
	for i in range(n - 1):
		board[1][i] = board[1][i + 1]
	board[1][n - 1] = tmp
	
	return board


def main():
	n, t = map(int, input().split())
	board = [[0] * n for _ in range(2)]
	for i in range(2):
		board[i] = list(map(int, input().split()))
	
	for i in range(t):
		board[1] = board[1][::-1]
		board = moveBoard(board, n)
		board[1] = board[1][::-1]
		
	for row in board:
		print(*row)


if __name__ == "__main__":
	main()