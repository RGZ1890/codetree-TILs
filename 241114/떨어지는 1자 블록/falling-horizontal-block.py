def moveable(board, n, block, r):
	if r >= n:
		return True
	for j in range(block[0], block[1]):
		if board[r][j] != 0:
			return False
	return True


def main():
	n, m, k = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	block = [k - 1, k + m - 1]
	
	for row in range(n):
		if not moveable(board, n, block, row + 1):
			for j in range(block[0], block[1]):
				board[row][j] = 1
			break
	
	for row in board:
		print(*row)


if __name__ == "__main__":
	main()