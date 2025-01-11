dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def travel(tboard, board, cur, cnt, ans):
	if tboard[cur[0]][cur[1]] == 0:
		return max(cnt, ans)
	for d in dirs:
		nex = [cur[0] + d[0], cur[1] + d[1]]
		if board[cur[0]][cur[1]] < board[nex[0]][nex[1]]:
			ans = travel(tboard, board, nex, cnt + 1, ans)
	
	return ans
	

def solution(board, n):
	tboard = [[0] * (n + 2) for _ in range(n + 2)]
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			cur = [i, j]
			for d in dirs:
				nex = [cur[0] + d[0], cur[1] + d[1]]
				if board[cur[0]][cur[1]] < board[nex[0]][nex[1]]:
					tboard[cur[0]][cur[1]] += 1
	
#	for row in tboard:
#		print(row)
	
	ans = 0
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			ans = travel(tboard, board, [i, j], 1, ans)
			
	return ans


def main():
	n = int(input())
	board = [[0] * (n + 2) for _ in range(n + 2)]
	for i in range(1, n + 1):
		board[i] = [0] + list(map(int, input().split())) + [0]

	print(solution(board, n))


if __name__ == "__main__":
	main()