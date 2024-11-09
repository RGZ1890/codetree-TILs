def explode(board, n, r, c):
	dist = board[r][c]
	for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
		for i in range(dist):
			nr, nc = r + d[0] * i, c + d[1] * i
			if 0 <= nr < n and 0 <= nc < n:
				board[nr][nc] = 0
			else:
				break
	
	return board


def affect(board, n):
	for j in range(n):
		i = n - 1
		for k in range(n - 1, -1, -1):
			if board[k][j] != 0:
				if i != k:
					board[i][j], board[k][j] = board[k][j], 0
				i -= 1
				
	return board


def main():
	n = int(input())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
		
	r, c = map(int, input().split())
	board = explode(board, n, r - 1, c - 1)
	board = affect(board, n)
	
	for row in board:
		print(*row)


if __name__ == "__main__":
	main()