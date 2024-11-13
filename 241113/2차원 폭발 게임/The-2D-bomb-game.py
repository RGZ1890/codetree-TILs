from collections import deque


def getSum(board, N):
	ret = 0
	for j in range(N):
		for i in range(N - 1, -1, -1):
			if board[i][j] == 0:
				break
			ret += 1
	
	return ret


def explode(board, N, M):
	while True:
		cont = False
		for j in range(N):
			queue = deque()
			streak = 1
			for i in range(N):
				if board[i][j] == 0 or M == 1:
					continue
				last = queue[-1] if queue else -1
				
				if last == board[i][j]:
					queue.append(board[i][j])
					streak += 1
					if i == N - 1 and streak >= M:
						cont = True
						for _ in range(streak):
							queue.pop()
				else:
					if streak >= M:
						cont = True
						for _ in range(streak):
							queue.pop()
					queue.append(board[i][j])
					streak = 1
			
			tmp = [0] * (N - len(queue)) + list(queue)
			for i in range(N):
				board[i][j] = tmp[i]
				
		if not cont:
			break

							
	return board


def rotate(board, N):
	board = [[board[i][j] for i in range(N - 1, -1, -1)] for j in range(N)]
	for j in range(N):
		queue = deque()
		for i in range(N):
			if board[i][j] != 0:
				queue.append(board[i][j])
		tmp = [0] * (N - len(queue)) + list(queue)
		for i in range(N):
			board[i][j] = tmp[i]

	return board


def main():
	N, M, K = map(int, input().split())
	board = [[0] * N for _ in range(N)]
	for i in range(N):
		board[i] = list(map(int, input().split()))
		
	for _ in range(K):
		board = explode(board, N, M)
		board = rotate(board, N)
	
	board = explode(board, N, M)
		
	answer = getSum(board, N)
	print(answer)
	

if __name__ == "__main__":
	main()