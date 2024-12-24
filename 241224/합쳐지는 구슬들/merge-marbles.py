dirs = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}

def move(n, marbles, m):
	for i in range(m):
		nex = [marbles[i][0] + marbles[i][2], marbles[i][1] + marbles[i][3]]
		if 0 <= nex[0] < n and 0 <= nex[1] < n:
			marbles[i][0], marbles[i][1] = nex[0], nex[1]
		else:
			marbles[i][2], marbles[i][3] = -marbles[i][2], -marbles[i][3]
	
	return marbles


def combine(marbles, m):
	for i in range(m):
		for j in range(i):
			if (marbles[i][0], marbles[i][1]) == (marbles[j][0], marbles[j][1]):
				marbles[j][0], marbles[j][1] = -1, -1
				marbles[i][4] += marbles[j][4]
				break
	
	marbles = [m for m in marbles if m[0] != -1]
	
	return marbles
		

def solution(n, marbles, m, t):
	cnt = len(marbles)
	for _ in range(t):
		marbles = move(n, marbles, cnt)
		marbles = combine(marbles, cnt)
		cnt = len(marbles)
	
	weight = max(marbles, key = lambda m: m[4])[4]
	
	return cnt, weight


def main():
	n, m, t = map(int, input().split())
	marbles = [[-1, -1, 0, 0, 0] for _ in range(m)]
	for i in range(m):
		r, c, d, w = input().split()
		marbles[i] = [int(r) - 1, int(c) - 1, dirs[d][0], dirs[d][1], int(w)]
	
	cnt, weight = solution(n, marbles, m, t)
	print(cnt, weight)
		

if __name__ == "__main__":
	main()