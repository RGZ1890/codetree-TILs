dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def turn(d, bound):
	if bound == 'L':
		return 3 if d == 0 else d - 1
	return 0 if d == 3 else d + 1


def move(board, N, cpos, cdir):
	npos = [cpos[0] + dirs[cdir][0], cpos[1] + dirs[cdir][1]]
#	print(cpos, npos, cdir)
	if board[npos[0]][npos[1]] == 1:
		cdir = turn(cdir, 'L')
		return move(board, N, cpos, cdir)
	elif board[npos[0]][npos[1]] == 0:
		ndir = turn(cdir, 'R')
		nnpos = [npos[0] + dirs[ndir][0], npos[1] + dirs[ndir][1]]
		if board[nnpos[0]][nnpos[1]] == 1:
			return npos, cdir
		return npos, ndir
	return npos, cdir


def trav(board, N, cpos, start):
	t = 0
	cdir = 1
	while True:
		t += 1
		npos, ndir = move(board, N, cpos, cdir)
		if board[npos[0]][npos[1]] == -1:
			break
		if npos == start:
			return -1
		cpos, cdir = npos, ndir
	
	return t


def main():
	N = int(input())
	board = [[-1] * (N + 2) for _ in range(N + 2)]
	x, y = map(int, input().split())
	start = cur = [x, y]

	for i in range(1, N + 1):
		s = input()
		for j in range(N):
			board[i][j + 1] = 1 if s[j] == '#' else 0
	
	answer = trav(board, N, cur, start)
	
	print(answer)
		


if __name__ == "__main__":
	main()