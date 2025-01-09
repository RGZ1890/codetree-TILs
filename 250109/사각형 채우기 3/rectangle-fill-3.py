DP = [-1] * 1001
DP[0], DP[1], DP[2], DP[3] = 0, 2, 7, 22

def solution(N):
	if DP[N] != -1:
		return DP[N]
	
	DP[N] = solution(N - 1) * 3 + (solution(N - 2) - solution(N - 3))
	DP[N] %= 1000000007
	return DP[N]


def main():
	n = int(input())
	print(solution(n))


if __name__ == "__main__":
	main()