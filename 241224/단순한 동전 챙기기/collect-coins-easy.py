INF = 400

def solution(N, coins, bef, cur, move, cnt, ans):
	if move >= ans:
		return ans
	
	if cur == 10:
		return move if cnt >= 4 else ans
	
	next = cur + 1
	if next != 10:
		ans = solution(N, coins, bef, next, move, cnt, ans)
	if coins[next] != [-1, -1]:
		newdist = abs(coins[next][1] - coins[bef][1]) \
				+ abs(coins[next][0] - coins[bef][0])
				
		ans = solution(N, coins, next, next, move + newdist, cnt + 1, ans)
	
	return ans


def main():
	N = int(input())
	coins = [[-1, -1] for _ in range(11)]
	for i in range(N):
		tmp = input()
		for j in range(N):
			if tmp[j] == 'S':
				coins[0] = [i, j]
			elif tmp[j] == 'E':
				coins[10] = [i, j]
			elif tmp[j] != '.':
				coins[int(tmp[j])] = [i, j]
	
	answer = solution(N, coins, 0, 0, 0, 0, INF)
	print(answer if answer != INF else -1)


if __name__ == "__main__":
	main()