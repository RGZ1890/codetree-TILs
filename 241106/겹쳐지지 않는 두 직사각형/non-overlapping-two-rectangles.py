def getSum(board, start, end):
	s = 0
	for i in range(start[0], end[0]):
		for j in range(start[1], end[1]):
			if board[i][j] == -1001:
				return -1001
			s += board[i][j]
	return s


def setBoard(board, start, end):
	subBoard = [[cell for cell in row] for row in board]
	for i in range(start[0], end[0]):
		for j in range(start[1], end[1]):
			subBoard[i][j] = -1001
	
	return subBoard

def getArea2(subBoard, n, m, s1):
	s2 = -1001
	for sr2 in range(n):
		for sc2 in range(m):
			start2 = [sr2, sc2]
			for er2 in range(sr2 + 1, n + 1):
				for ec2 in range(sc2 + 1, m + 1):
					end2 = [er2, ec2]
#					print('\t2', start2, end2, getSum(subBoard, start2, end2), end = ' ')
					s2 = max(getSum(subBoard, start2, end2), s2)
#					print(s1 + s2)
					
	return s2


def getArea(board, n, m):
	res = -1001 * 2
	for sr1 in range(n):
		for sc1 in range(m):
			start1 = [sr1, sc1]
			for er1 in range(sr1 + 1, n + 1):
				for ec1 in range(sc1 + 1, m + 1):
					end1 = [er1, ec1]
					s1 = getSum(board, start1, end1)
#					print('1', start1, end1, s1)
					subBoard = setBoard(board, start1, end1)
					s2 = getArea2(subBoard, n, m, s1)
					
					res = max(s1 + s2, res)
									
	return res


def main():
	n, m = map(int, input().split())
	board = [[0] * m for _ in range(n)]
	for i in range(n):
		board[i] = list(map(int, input().split()))
	
	answer = getArea(board, n, m)
	
	print(answer)
						
	
if __name__ == "__main__":
	main()