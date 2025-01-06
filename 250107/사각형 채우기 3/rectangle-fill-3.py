DP = [0] * 1001
DP[1], DP[2] = 2, 7

def solution(N):
	if DP[N] != 0:
		return DP[N]
	DP[N] = (1 * solution(N - 1) + (N - 1) * solution(1) \
			+ 2 * solution(N - 2) + (N - 2) * solution(2)) \
		% 1000000007
	return DP[N]


def main():
	n = int(input())
	print(solution(n))


if __name__ == "__main__":
	main()