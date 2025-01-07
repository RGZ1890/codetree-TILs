memo = [0] * 20
memo[0], memo[1], memo[2], memo[3] = 1, 1, 2, 5

def DP(n):
	if memo[n] != 0:
		return memo[n]
	
	for rt in range(1, n + 1):
		memo[n] += DP(rt - 1) * DP(n - rt)
	return memo[n]


def main():
	N = int(input())
	print(DP(N))
	

if __name__ == "__main__":
	main()