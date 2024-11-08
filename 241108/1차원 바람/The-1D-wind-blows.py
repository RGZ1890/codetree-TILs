def blow(board, M, cur, d, affected):
	if d:
		board[cur] = board[cur][1:M] + [board[cur][0]]
	else:
		board[cur] = [board[cur][M - 1]] + board[cur][0:M - 1]
	
#	print(cur, "--------------")
#	for row in board:
#		print(*row)
	
	return prop(board, M, cur, not d, affected)
	

def prop(board, M, cur, d, affected):
	upper, lower = cur - 1 in affected, cur + 1 in affected
	for i in range(M):
		cell = board[cur][i]
		if not upper and board[cur - 1][i] == cell:
			upper = True
			affected.append(cur - 1)
			board = blow(board, M, cur - 1, d, affected)
		if not lower and board[cur + 1][i] == cell:
			lower = True
			affected.append(cur + 1)
			board = blow(board, M, cur + 1, d, affected)
		if lower and upper:
			break
	
	return board


def main():
	N, M, Q = map(int, input().split())
	board = [[-1] * M for _ in range(N + 2)]
	for i in range(1, N + 1):
		board[i] = list(map(int, input().split()))
	
	for i in range(Q):
		r, d = input().split()
		r = int(r)
		d = True if d == 'R' else False
		board = blow(board, M, r, d, [r])
	
	for i in range(1, N + 1):
		print(*board[i])


if __name__ == "__main__":
	main()