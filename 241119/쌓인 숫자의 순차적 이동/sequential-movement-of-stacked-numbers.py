dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]


def move(board, n, cur):
	ret = cur
	val = 0
	for d in dirs:
		nex = [cur[0] + d[0], cur[1] + d[1]]
		if 0 <= nex[0] < n and 0 <= nex[1] < n and board[nex[0]][nex[1]]:
			if max(board[nex[0]][nex[1]]) > val:
				val = max(board[nex[0]][nex[1]])
				ret = nex
				
	return ret


def updateBoard(board, numbers, tgt, cur, ret):
	idx = 0
	for i in range(len(board[cur[0]][cur[1]])):
		numbers[board[cur[0]][cur[1]][i]] = [ret[0], ret[1]]
		if board[cur[0]][cur[1]][i] == tgt:
			idx = i
			board[ret[0]][ret[1]] = board[cur[0]][cur[1]][:i + 1] + board[ret[0]][ret[1]]
			board[cur[0]][cur[1]] = board[cur[0]][cur[1]][i + 1:]
			break
	
	return board, numbers


def main():
	n, m = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	numbers = [[0, 0] for _ in range(n ** 2 + 1)]
	for i in range(n):
		lis = list(map(int, input().split()))
		for j in range(n):
			board[i][j] = [lis[j]]
			numbers[board[i][j][0]] = [i, j]
	targets = list(map(int, input().split()))
	

	
	for tgt in targets:
		cur = numbers[tgt]
		ret = move(board, n, cur)
		board, numbers = updateBoard(board, numbers, tgt, cur, ret)
		
	
	for row in board:
		for cell in row:
			if cell:
				print(*cell)
			else:
				print("None")
		
#		print("==============", tgt)
#		for row in board:
#			print(*row)
	

if __name__ == "__main__":
	main()