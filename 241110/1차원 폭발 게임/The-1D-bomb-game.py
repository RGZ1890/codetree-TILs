def explode(stac, l, M):
	i = 1
	s, e = 0, -1
	for i in range(l):
		if stac[s] == stac[i]:
			e = i
		else:
			if e - s + 1 >= M:
				return s, e
			else:
				s = i
		
	return s, e


def exclude(stac, l, s, e):
	tmp = [0] * (len(stac) - (e - s + 1))
	j = 0
	for i in range(l):
		if not (s <= i <= e):
			tmp[j] = stac[i]
			j += 1
			
	return tmp


def main():
	N, M = map(int, input().split())
	stac = [0] * N
	for i in range(N):
		stac[i] = int(input())
	
	
	while True:
		l = len(stac)
		s, e = explode(stac, l, M)
		if s - e + 1 >= M or l < M:
			break
		stac = exclude(stac, l, s, e)
	
	l = len(stac)
	print(l)
	for i in range(l):
		print(stac[i])
	

if __name__ == "__main__":
	main()