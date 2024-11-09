def explode(board, n, r, c):
	dist = board[r][c] - 1
	board[r][c] = 0
	for d in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
		cur = [r, c]
		for i in range(dist):
			cur = [cur[0] + d[0], cur[1] + d[1]]
			if not (0 <= cur[0] < n and 0 <= cur[1] < n):
				break
			board[cur[0]][cur[1]] = 0
	
	return board


def affect(board, n):
	for j in range(n):
		tmp = [0] * n
		i = n - 1
		for k in range(n - 1, -1, -1):
			if board[k][j] != 0:
				tmp[i] = board[k][j]
				i -= 1
		for l in range(n):
			board[l][j] = tmp[l]
	
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