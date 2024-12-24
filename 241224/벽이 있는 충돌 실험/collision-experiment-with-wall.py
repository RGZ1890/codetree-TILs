dirs = {'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]}


def move(N, marble):
	nx, ny = marble[0] + marble[2], marble[1] + marble[3]
	if 0 <= nx < N and 0 <= ny < N:
		marble[0], marble[1] = nx, ny
	else:
		marble[2], marble[3] = -marble[2], -marble[3]


def solution(N, marbles):
	for _ in range(2 * N):
		positions = {}
		for m in marbles:
			move(N, m)
			pos = (m[0], m[1])
			if pos in positions:
				positions[pos].append(m)
			else:
				positions[pos] = [m]
				
		marbles = [m[0] for m in positions.values() if len(m) == 1]
		
		if not marbles:
			break
		
	return len(marbles)

def main():
	T = int(input())
	for _ in range(T):
		N, M = map(int, input().split())
		marbles = [[-1, -1, -1] for _ in range(M)]
		for i in range(M):
			s = input().split()
			marbles[i] = [int(s[0]) - 1, int(s[1]) - 1, dirs[s[2]][0], dirs[s[2]][1]]
		
		answer = solution(N, marbles)
		print(answer)
		

if __name__ == "__main__":
	main()