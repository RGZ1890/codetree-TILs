memo = [0] * 1001
memo[1], memo[2] = 1, 3


def DP(n):
	if memo[n] != 0:
		return memo[n]
	
	memo[n] = DP(n - 2) * 2 + DP(n - 1)
	memo[n] %= 10007
	return memo[n]


def main():
	n = int(input())
	print(DP(n))
	

if __name__ == "__main__":
	main()