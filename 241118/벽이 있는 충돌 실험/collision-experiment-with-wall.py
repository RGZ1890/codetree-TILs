ddict = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def avail(beed):
	return beed[0] != -1


def move(N, beed):
	d = beed[2]
	nex = [beed[0] + dirs[d][0], beed[1] + dirs[d][1]]
	if 0 <= nex[0] < N and 0 <= nex[1] < N:
		return [nex[0], nex[1], beed[2]]
	
	d = 4 - d if (d % 2) else 2 - d
	return [beed[0], beed[1], d]


def updatebeeds(beeds, M):
	for i in range(M):
		if avail(beeds[i]):
			cur = beeds[i]
			for j in range(M):
				if i != j and (cur[0] == beeds[j][0] and cur[1] == beeds[j][1]):
					beeds[i] = beeds[j] = [-1, -1, -1]
	
	return beeds
				

def main():
	T = int(input())
	for _ in range(T):
		N, M = map(int, input().split())
		
		beeds = [[0] * 3 for _ in range(M)]
		for i in range(M):
			x, y, d = input().split()
			beeds[i][0], beeds[i][1], beeds[i][2] = int(x) - 1, int(y) - 1, ddict[d]
		
		answer = 0
		for _ in range(N ** 2 + 1):
			for i in range(M):
				if avail(beeds[i]):
					beeds[i] = move(N, beeds[i])
			beeds = updatebeeds(beeds, M)
			
			answer = 0
			for i in range(M):
				answer += 1 if avail(beeds[i]) else 0
			if answer == 1:
				break
		
		if answer != 1:
			answer = 0
			for i in range(M):
				answer += 1 if avail(beeds[i]) else 0
		print(answer)


if __name__ == "__main__":
	main()