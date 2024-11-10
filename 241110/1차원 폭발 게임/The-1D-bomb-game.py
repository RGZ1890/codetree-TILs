def explode(stac, l, M):
	i = 1
	s, e = 0, -1
	while i < len(stac):
		if stac[s] == stac[i]:
			e = i
		else:
			if e - s + 1 >= M:
#				print("___________", s, e, stac)
				stac = exclude(stac, len(stac), s, e)
				s, e, i = 0, -1, 0
			else:
				s = i
		i += 1
		
	return stac[:-1]


def exclude(stac, l, s, e):
	tmp = []
	for i in range(l):
		if s <= i <= e:
			continue
		tmp.append(stac[i])
			
	return tmp


def main():
	N, M = map(int, input().split())
	stac = [0] * N
	for i in range(N):
		stac[i] = int(input())
	
	stac += [0]
	
	l = len(stac)
	stac = explode(stac, l, M)
	
	l = len(stac)
	print(l)
	for i in range(l):
		print(stac[i])
	

if __name__ == "__main__":
	main()