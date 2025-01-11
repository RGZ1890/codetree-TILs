dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def moveable(board, n, cur, nex):
	return board[nex[0]][nex[1]] != 0 and board[cur[0]][cur[1]] > board[nex[0]][nex[1]]


def travel(aboard, board, n, cur):
	if aboard[cur[0]][cur[1]] != 0:
		return aboard[cur[0]][cur[1]]
	cnt = 1
	for d in dirs:
		nex = [cur[0] + d[0], cur[1] + d[1]]
		if moveable(board, n, cur, nex):
			cnt = max(cnt, travel(aboard, board, n, nex) + 1)
	aboard[cur[0]][cur[1]] = cnt
	
	return aboard[cur[0]][cur[1]]
		

def solution(board, n):
	aboard = [[0] * (n + 2) for _ in range(n + 2)]
	
	ans = 0
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			ans = max(ans, travel(aboard, board, n, [i, j]))
			
	return ans


def main():
	n = int(input())
	board = [[0] * (n + 2) for _ in range(n + 2)]
	for i in range(1, n + 1):
		board[i] = [0] + list(map(int, input().split())) + [0]

	print(solution(board, n))


if __name__ == "__main__":
	main()