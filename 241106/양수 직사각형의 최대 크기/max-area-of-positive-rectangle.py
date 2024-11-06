def checkArea(board, sr, sc, er, ec):
	for r in range(sr, er):
		for c in range(sc, ec):
			if board[r][c] <= 0:
				return -1
	return (er - sr) * (ec - sc)


def getArea(board, n, m):
	size = -1
	for sr in range(n):
		for sc in range(m):
			if board[sr][sc] <= 0:
				continue
			for er in range(sr + 1, n + 1):
				for ec in range(sc + 1, m + 1):
					if board[er - 1][ec - 1] <= 0:
						continue
					size = max(checkArea(board, sr, sc, er, ec), size)
	return size


def main():
	n, m = map(int, input().split())
	board = [[0] * m for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	answer = getArea(board, n, m)
	print(answer)	


if __name__ == "__main__":
	main()