def update(val, left, upper):
	n_left = [min(val, left[0]), max(val, left[1])]
	n_upper = [min(val, upper[0]), max(val, upper[1])]
	
	if (n_left[1] - n_left[0]) <= (n_upper[1] - n_upper[0]):
		if n_left[1] - n_left[0] == n_upper[1] - n_upper[0] \
		and left[1] - left[0] > upper[1] - upper[0]:
			return n_upper
		return n_left
	return n_upper


def solution(board, n):
	aboard = [[[0, 101] for _ in range(n + 2)] for _ in range(n + 2)]
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			if [i, j] == [1, 1]:
				aboard[i][j] = [board[i - 1][j - 1], board[i - 1][j - 1]]
				continue
			aboard[i][j] = update(board[i - 1][j - 1], aboard[i][j - 1], aboard[i - 1][j])

#	for row in aboard:
#		print(row)

	return aboard[n][n][1] - aboard[n][n][0]


def main():
	n = int(input())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	print(solution(board, n))


if __name__ == "__main__":
	main()