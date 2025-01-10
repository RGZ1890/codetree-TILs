NOPE = 1000001

def getVal(ans_board, cur, cand):
	return min(ans_board[cur[0]][cur[1]], ans_board[cand[0]][cand[1]])


def solution(board, N):
	ans_board = [[NOPE] * (N + 2) for _ in range(N + 2)]
	for i in range(1, N + 1):
		ans_board[i] = [NOPE] + board[i - 1] + [NOPE]
	
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			if [i, j] == [1, 1]:
				continue
			cur, left, upper = [i, j], [i - 1, j], [i, j - 1]
			ans_board[i][j] = max(getVal(ans_board, cur, upper), getVal(ans_board, cur, left))
	
	return ans_board[N][N]


def main():
	N = int(input())
	board = [[0] * N for _ in range(N)]
	for i in range(N):
		board[i] = list(map(int, input().split()))
	
	print(solution(board, N))


if __name__ == "__main__":
	main()