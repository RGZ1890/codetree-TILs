directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def realign(board, n):
	for j in range(n):
		for i in range(n - 2, -1, -1):
			if board[i + 1][j] == 0:
				board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
				
	return board

def explode(board, n, start):
	dist = board[start[0]][start[1]]
	board[start[0]][start[1]] = 0
	for i in range(4):
		d = directions[i]
		for j in range(1, dist):
			pos = [start[0] + d[0] * j, start[1] + d[1] * j]
			if 0 <= pos[0] < n and 0 <= pos[1] < n:
				board[pos[0]][pos[1]] = 0
			else:
				break
		
	return realign(board, n)


def main():
	n, m = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	for _ in range(m):
		c = int(input()) - 1
		for i in range(n):
			if board[i][c] != 0:
				board = explode(board, n, [i, c])
				break
		
	for row in board:
		print(*row)
	

if __name__ == "__main__":
	main()