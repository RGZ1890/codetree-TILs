def explode(stac, l, M):
	i = 1
	s, e = 0, -1
	coor = []
	for i in range(l):
		if stac[s] == stac[i]:
			e = i
		else:
			if e - s + 1 >= M:
				coor.append([s, e])
			s, e = i, -1
		
	return coor


def exclude(stac, l, coor):
	tmp = []
	for i in range(l):
		isIn = False
		for c in coor:
			if c[0] <= i <= c[1]:
				isIn = True
				break
		if not isIn:
			tmp.append(stac[i])
			
	return tmp


def main():
	N, M = map(int, input().split())
	stac = [0] * (N + 1)
	for i in range(N):
		stac[i] = int(input())
	
	while True:
		l = len(stac)
		coor = explode(stac, l, M)
		if not coor:
			break
		stac = exclude(stac, l, coor)
	
	stac = stac[:-1]
	
	l = len(stac)
	print(l)
	for i in range(l):
		print(stac[i])
	

if __name__ == "__main__":
	main()