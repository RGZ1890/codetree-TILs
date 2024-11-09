directions = [[-1, 1], [-1, -1], [1, -1], [1, 1]]

def trav(board, start, m):
	path = []
	cur = [start[0], start[1]]
	for i in range(4):
		for j in range(m[i]):
			path.append(cur)
			cur = [cur[0] + directions[i][0], cur[1] + directions[i][1]]
	
	return path


def rotBoard(board, path, start, l, d):
	if d == 1:
		tmp = board[start[0]][start[1]]
		for i in range(l - 1):
			board[path[i][0]][path[i][1]] = board[path[i + 1][0]][path[i + 1][1]]
		board[path[l - 1][0]][path[l - 1][1]] = tmp
	else:
		tmp = board[path[l - 1][0]][path[l - 1][1]]
		for i in range(l - 1, 0, -1):
			board[path[i][0]][path[i][1]] = board[path[i - 1][0]][path[i - 1][1]]
		board[start[0]][start[1]] = tmp
	
	return board
	

def main():
	n = int(input())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	r, c, m1, m2, m3, m4, d = map(int, input().split())
	start = [r - 1, c - 1]
	m = [m1, m2, m3, m4]
	path = trav(board, start, m)
#	print(path)
	l = sum(m)
	board = rotBoard(board, path, start, l, d)
	
	for row in board:
		print(*row)
		

if __name__ == "__main__":
	main()