def rotBoard(board, n):
	left = board[2][n - 1]
	middle = board[0][n - 1]
	right = board[1][n - 1]
	
	for i in range(3):
		for j in range(n - 2, -1, -1):
			board[i][j + 1] = board[i][j]
	board[0][0] = left
	board[1][0] = middle
	board[2][0] = right
	
	return board


def main():
	n, t = map(int, input().split())
	board = [[0] * n for _ in range(3)]
	for i in range(3):
		board[i] = list(map(int, input().split()))
		
	for i in range(t):
		board = rotBoard(board, n)
	
	for row in board:
		print(*row)


if __name__ == "__main__":
	main()