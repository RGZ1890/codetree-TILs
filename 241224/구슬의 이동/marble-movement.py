ddict = {"U": 0, "R": 1, "D": 2, "L": 3}
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def move(marble, n):
	cdir = marble[2]
	for _ in range(marble[3]):
		nex = [marble[0] + dirs[cdir][0], marble[1] + dirs[cdir][1]]
		if not (0 <= nex[0] < n and 0 <= nex[1] < n):
			cdir = 4 - cdir if (cdir % 2 == 1) else 2 - cdir
			nex = [marble[0] + dirs[cdir][0], marble[1] + dirs[cdir][1]]
		marble[0], marble[1], marble[2] = nex[0], nex[1], cdir
	
	return marble


def cntMarbles(marbles, m, k):
	res = []
	for i in range(m):
		if marbles[i][0] == -1:
			continue
		cur = [marbles[i][0], marbles[i][1]]
		coll = set()
		for j in range(m):
			if cur[0] == marbles[j][0] and cur[1] == marbles[j][1] and i != j:
				coll.add(i)
				coll.add(j)
		if len(coll) > k and coll not in res:
			res.append(coll)
	
	return res


def checkCollide(marbles, m, k):
	res = cntMarbles(marbles, m, k)
	for rs in res:
		lis = [marbles[r] for r in rs]
		lis = sorted(lis, key = lambda x: (x[3], x[4]), reverse = True)
		
		for i in range(k, len(lis)):
			marbles[lis[i][4]] = [-1, -1, -1, -1, -1]
			
	return marbles


def main():
	n, m, t, k = map(int, input().split())
	marbles = [[-1, -1, -1, -1] for _ in range(m)]
	for i in range(m):
		r, c, d, v = input().split()
		marbles[i] = [int(r) - 1, int(c) - 1, ddict[d], int(v), i]
	
	for _ in range(t):
		for i in range(m):
			if marbles[i][0] != -1:
				marbles[i] = move(marbles[i], n)
		
		marbles = checkCollide(marbles, m, k)
		
#		print(*marbles)


	answer = 0
	for m in marbles:
		answer += 1 if m[0] != -1 else 0
	print(answer)

if __name__ == "__main__":
	main()