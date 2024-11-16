dirs = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}


def move(board, N, snake, d):
	dest = [snake[0][0] + dirs[d][0], snake[0][1] + dirs[d][1]]
	if 0 <= dest[0] < N and 0 <= dest[1] < N:
		l = len(snake)
		if board[dest[0]][dest[1]] == 1:
			board[dest[0]][dest[1]] = 0
			snake = [dest] + snake
			if dest in snake[1:]:
				return board, []
		else:
			snake = [dest] + snake[:l - 1]
			if dest in snake[1:]:
				return board, []
		
		return board, snake
	
	return board, []


def main():
	N, M, K = map(int, input().split())
	board = [[0] * N for _ in range(N)]
	for _ in range(M):
		x, y = map(int, input().split())
		board[x - 1][y - 1] = 1
	
	
	
	snake = [[0, 0]]
	answer = 0
	for _ in range(K):
		s = input().split()
		d, p = s[0], int(s[1])
		for _ in range(p):
			answer += 1
			board, snake = move(board, N, snake, d)
			print("ANSWER", answer)
			print("SNAKE", snake)
			if not snake:
				break
		if not snake:
			break
	
	print(answer)
	
	
if __name__ == "__main__":
	main()