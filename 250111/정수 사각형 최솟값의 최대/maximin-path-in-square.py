NOPE = 1000001


def solution(board, N):
	sboard = [[NOPE] * (N + 2) for _ in range(N + 2)]
	for i in range(1, N + 1):
		sboard[i] = [NOPE] + board[i - 1] + [NOPE]
	
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			if [i, j] == [1, 1]:
				continue
			sboard[i][j] = min(sboard[i][j], max(sboard[i - 1][j], sboard[i][j - 1]))
		
	return sboard[N][N]
	

def main():
	N = int(input())
	board = [[0] * N for _ in range(N)]
	
	for i in range(N):
		board[i] = list(map(int, input().split()))
	
	print(solution(board, N))


if __name__ == "__main__":
	main()