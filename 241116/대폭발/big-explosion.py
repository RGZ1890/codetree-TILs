dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def explode(board, n, bombs, bomb, t):
	dist = 2 ** (t - 1)
	for d in dirs:
		nex = [bomb[0] + d[0] * dist, bomb[1] + d[1] * dist]
		if 0 <= nex[0] < n and 0 <= nex[1] < n \
		and board[nex[0]][nex[1]] == 0:
			bombs.append(nex)
			board[nex[0]][nex[1]] = 1
	return bombs


def main():
	n, m, r, c = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	board[r - 1][c - 1] = 1
	bombs = [[r - 1, c - 1]]
	
	for t in range(1, m + 1):
		l = len(bombs)
		for i in range(l):
			bombs = explode(board, n, bombs, bombs[i], t)
#		print("bomb", bombs)
#		for row in board:
#			print(*row)
			
	answer = sum([sum(row) for row in board])
	print(answer)

if __name__ == "__main__":
	main()