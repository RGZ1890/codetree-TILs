dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def avail(beed):
	return beed[0] != 0


def move(board, n, cur):
	ret = cur
	val = 0
	for d in dirs:
		nex = [cur[0] + d[0], cur[1] + d[1]]
		if board[nex[0]][nex[1]] > val:
			val = board[nex[0]][nex[1]]
			ret = nex
	
	return ret


def updatebeeds(beeds, m):
	for i in range(m):
		cur = beeds[i]
		if avail(cur):
			for j in range(m):
				if i != j and beeds[j] == cur:
					beeds[i] = beeds[j] = [0, 0]
	
	return beeds
	

def main():
	n, m, t = map(int, input().split())
	board = [[0] * (n + 2) for _ in range(n + 2)]
	for i in range(1, n + 1):
		board[i] = [0] + list(map(int, input().split())) + [0]
	beeds = [[0, 0] for _ in range(m)]
	for i in range(m):
		beeds[i] = list(map(int, input().split()))
		
	for _ in range(t):
		for i in range(m):
			if avail(beeds[i]):
				beeds[i] = move(board, n, beeds[i])
		beeds = updatebeeds(beeds, m)
#		print(_, *beeds)
	
	answer = 0
	for b in beeds:
		answer += 1 if avail(b) else 0
	print(answer)
		

if __name__ == "__main__":
	main()