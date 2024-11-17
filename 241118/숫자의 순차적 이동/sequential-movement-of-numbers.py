dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def move(board, n, numbers, i):
	cur = numbers[i]
	tpos, tval = [], 0
	for d in dirs:
		nex = [cur[0] + d[0], cur[1] + d[1]]
		if board[nex[0]][nex[1]] > tval:
			tval = board[nex[0]][nex[1]]
			tpos = nex
	board[cur[0]][cur[1]], board[tpos[0]][tpos[1]] = tval, i
	numbers[i], numbers[tval] = tpos, cur
	
	return board, numbers


def main():
	n, m = map(int, input().split())
	board = [[0] * (n + 2) for _ in range(n + 2)]
	numbers = [[-1, -1] for _ in range(n ** 2 + 1)]
	for i in range(1, n + 1):
		board[i] = [0] + list(map(int, input().split())) + [0]
		for j in range(1, n + 1):
			numbers[board[i][j]] = [i, j]
	
	for _ in range(m):
		for i in range(1, n ** 2 + 1):
			board, numbers = move(board, n, numbers, i)
		
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			print(board[i][j], end = ' ')
		print()
		


if __name__ == "__main__":
	main()