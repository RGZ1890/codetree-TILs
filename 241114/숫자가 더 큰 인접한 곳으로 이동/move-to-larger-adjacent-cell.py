directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def move(board, n, cur):
	for d in directions:
		nex = [cur[0] + d[0], cur[1] + d[1]]
		if 0 <= nex[0] < n and 0 <= nex[1] < n and \
		board[nex[0]][nex[1]] > board[cur[0]][cur[1]]:
			return nex
	return []


def main():
	n, r, c = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	cur = [r - 1, c - 1]
	
	while True:
		print(board[cur[0]][cur[1]], end = ' ')
		nex = move(board, n, cur)
		if not nex:
			break
		cur = nex


if __name__ == "__main__":
	main()