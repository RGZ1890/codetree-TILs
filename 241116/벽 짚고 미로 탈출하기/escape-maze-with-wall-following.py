dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def move(board, cpos, cdir):
	npos = [cpos[0] + dirs[cdir][0], cpos[1] + dirs[cdir][1]]
	if board[npos[0]][npos[1]] == 1:
		for i in range(3):
			cdir = cdir - 1 if cdir > 0 else 3
			npos = [cpos[0] + dirs[cdir][0], cpos[1] + dirs[cdir][1]]
			if board[npos[0]][npos[1]] == 1:
				npos = cpos
			else:
				break
	elif board[npos[0]][npos[1]] == 0:
		ndir = cdir + 1 if cdir < 3 else 0
		nnpos = [npos[0] + dirs[ndir][0], npos[1] + dirs[ndir][1]]
		if board[nnpos[0]][nnpos[1]] == 0:
			return npos, ndir
		
	return npos, cdir



def main():
	N = int(input())
	board = [[-1] * (N + 2) for _ in range(N + 2)]
	cpos = start = list(map(int, input().split()))
	for i in range(1, N + 1):
		s = input()
		for j in range(1, N + 1):
			board[i][j] = 1 if s[j - 1] == '#' else 0
			
	answer = 0
	sdir = cdir = 1
	
	while True:
		answer += 1
		npos, ndir = move(board, cpos, cdir)
#		print(cpos, cdir, '->', npos, ndir)
		if (npos == start and cdir == sdir) or npos == cpos:
			answer = -1
			break
		elif board[npos[0]][npos[1]] == -1:
			break
		cpos, cdir = npos, ndir

	print(answer)


if __name__ == "__main__":
	main()