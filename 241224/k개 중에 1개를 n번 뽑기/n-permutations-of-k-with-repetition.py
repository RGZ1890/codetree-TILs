
def comb(K, N, cur, cnt):
	if cnt == N:
		print(*cur)
		return
	
	for i in range(1, K + 1):
		comb(K, N, cur + [i], cnt + 1)
		

def main():
	K, N = map(int, input().split())
	comb(K, N, [], 0)


if __name__ == "__main__":
	main()