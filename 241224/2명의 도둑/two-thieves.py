INF = 10

def selectLine(tmpLine, l, i, visited, C, val, ans):
	if C < 0:
		return visited, -1
	if i == l:
#		print(tmpLine, "VISITED", visited, "VAL", val, "C", C)
		return visited, val
	
	tvisited, tval = selectLine(tmpLine, l, i + 1, visited, C, val, ans)
	if tval > ans:
		visited, ans = tvisited, tval
	v = tmpLine[i]
	if v <= C:
		tvisited, tval = selectLine(tmpLine, l, i + 1, visited + [i], C - v, val + (v ** 2), ans)
		if tval > ans:
			visited, ans = tvisited, tval
	
	return visited, ans


def steal(board, N, M, C):
	visited, ans = [[]], 0
	for i in range(N):
		for j in range(N):
			tmpLine = board[i][j:j + M]
			if INF in tmpLine:
				continue
			tvisited, tans = selectLine(tmpLine, len(tmpLine), 0, [], C, 0, ans)
			if tans > ans:
				visited, ans = [[i, t + j] for t in tvisited], tans
				
	return visited, ans


def main():
	N, M, C = map(int, input().split())
	board = [[0] * N for _ in range(N)]
	for i in range(N):
		board[i] = list(map(int, input().split()))
	
	visited1, ans1 = steal(board, N, M, C)
	
#	print(visited1)
	if len(visited1) > 0:
		start = visited1[0]
#		print(start[0], start[1], start[1] + M)
		for j in range(start[1], min(start[1] + M, N)):
			board[start[0]][j] = INF
	
	visited2, ans2 = steal(board, N, M, C)
				
#	print("ANS", visited1, visited2, ans1, ans2)
	print(ans1 + ans2)


if __name__ == "__main__":
	main()