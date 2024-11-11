def getSum(board, N):
	ret = 0
	for i in range(N):
		for j in range(N):
			if board[i][j] != 0:
				ret += 1
	
	return ret


def align(board, N):
	for j in range(N):
		zidx = N - 1
		for i in range(N - 1, -1, -1):
			if board[i][j] != 0:
				for k in range(zidx, i, -1):
					if board[k][j] == 0:
						board[i][j], board[k][j] = board[k][j], board[i][j]
						zidx = k - 1
						break
		
	return board


def explode(board, N, M):
	for j in range(N):
		s = 0
		coor = []
		for i in range(1, N + 1):
			if board[s][j] == 0:
				s = i
			if i == N or board[i][j] != board[s][j]:
				coor.append([s, i])
				s = i
		for c in coor:
			if c[1] - c[0] >= M:
				for k in range(c[0], c[1]):
					board[k][j] = 0
					
	return align(board, N)


def rotate(board, N):
	board = [[board[i][j] for i in range(N - 1, -1, -1)] for j in range(N)]
	
	
	return align(board, N)


def main():
	N, M, K = map(int, input().split())
	board = [[0] * N for _ in range(N)]
	for i in range(N):
		board[i] = list(map(int, input().split()))
	
	for _ in range(K):
		board = explode(board, N, M)
		board = rotate(board, N)
		
	answer = getSum(board, N)
	while True:
		board = explode(board, N, M)
		s = getSum(board, N)
		if answer == s:
			break
		answer = s
	
	
	print(answer)
	

if __name__ == "__main__":
	main()