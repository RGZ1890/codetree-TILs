def get_area(board, n, m, point, s):
	golds = 0
	for i in range(point[0] - s, point[0] + s + 1):
		c = s - abs(i - point[0])
		for j in range(point[1] - c, point[1] + c + 1):
			if 0 <= i < n and 0 <= j < n:
				golds += board[i][j]
	if golds * m >= (s ** 2) + ((s + 1) ** 2):
		return golds
	return -1
			

def main():
	n, m = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	ans = 0
	for i in range(n):
#		print("SIZE", i, end = ' ')
		for j in range(n):
			for k in range(n):
				res = get_area(board, n, m, [j, k], i)
#				print("START", [j, k], "GOLDS", res, end = ' ')
				ans = max(ans, res)
#		print()	
	print(ans)


if __name__ == "__main__":
	main()