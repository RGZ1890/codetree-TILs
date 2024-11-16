dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def move(board, cur, dir):
	t = 0
	while True:
		t += 1
		nex = [cur[0] + dirs[dir][0], cur[1] + dirs[dir][1]]
		val = board[nex[0]][nex[1]]
		if val == -1:
			break
		elif val == 1:
			dir += 1 if (dir == 0 or dir == 2) else -1
		elif val == 2:
			dir = 3 - dir
		cur = nex

	return t


def main():
	n = int(input())
	board = [[-1] * (n + 2) for _ in range(n + 2)]
	for i in range(1, n + 1):
		board[i] = [-1] + list(map(int, input().split())) + [-1]
	answer = -1
	for i in range(n + 2):
		answer = max(answer, move(board, [i, 0], 1))
		answer = max(answer, move(board, [0, i], 2))
		answer = max(answer, move(board, [i, n + 1], 3))
		answer = max(answer, move(board, [n + 1, i], 0))
	
	print(answer)

if __name__ == "__main__":
	main()