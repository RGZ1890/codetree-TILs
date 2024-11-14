from collections import deque

directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def explode(board, n, r, c):
	tmpBoard = [row[:] for row in board]
	dist = tmpBoard[r][c]
	tmpBoard[r][c] = 0
	for d in directions:
		for i in range(1, dist):
			nr, nc = r + d[0] * i, c + d[1] * i
			if 0 <= nr < n and 0 <= nc < n:
				tmpBoard[nr][nc] = 0
	
	for j in range(n):
		tmpList = []
		for i in range(n):
			if board[i][j] != 0:
				tmpList.append(board[i][j])
				
		tmpList = [0] * (n - len(tmpList)) + tmpList
		for i in range(n):
			tmpBoard[i][j] = tmpList[i]
	
	return cntBoard(tmpBoard, n)


def cntBoard(tmpBoard, n):
	res = 0
	for r in range(n):
		for c in range(n):
			if tmpBoard[r][c] != 0:
				for d in directions:
					nr, nc = r + d[0], c + d[1]
					if 0 <= nr < n and 0 <= nc < n and \
					tmpBoard[r][c] == tmpBoard[nr][nc]:
						res += 1
#						tmpBoard[nr][nc] = 0
				tmpBoard[r][c] = 0
				
	return res
					
			

def main():
	n = int(input())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	answer = -1
	for i in range(n):
		for j in range(n):
			res = explode(board, n, i, j)
			answer = max(answer, res)
			
	print(answer)


if __name__ == "__main__":
	main()