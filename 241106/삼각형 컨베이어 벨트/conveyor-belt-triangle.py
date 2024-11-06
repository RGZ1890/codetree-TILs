def main():
	n, t = map(int, input().split())
	board = [[0] * n for _ in range(3)]
	for i in range(3):
		board[i] = list(map(int, input().split()))
	
	allR = board[0] + board[1] + board[2]
	l = 3 * n
	for i in range(t):
		allR = [allR[l - 1]] + allR[:l - 1]
	
	for i in range(3):
		for j in range(n):
			print(allR[3 * i + j], end = ' ')
		print()


if __name__ == "__main__":
	main()