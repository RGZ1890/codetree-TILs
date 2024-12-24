INF = 20000

def eucl(m, picked, cnt):
	res = 0
	if cnt > m:
		return INF
	
	for i in range(cnt):
		for j in range(i + 1, cnt):
			dist_sq = (picked[i][1] - picked[j][1]) ** 2 + (picked[i][0] - picked[j][0]) ** 2
			res = max(res, dist_sq)
			
	return res


def pick(points, n, m, cur, dist, picked, cnt, ans):
	if cur == n:
#		print(picked if cnt == m else "NO", eucl(points, picked, m) if cnt == m else ans)
		return dist if cnt == m else ans
	
	newdist = eucl(m, picked + [points[cur]], cnt + 1)
	if newdist < ans:
		ans = pick(points, n, m, cur + 1, newdist, picked + [points[cur]], cnt + 1, ans)
	ans = pick(points, n, m, cur + 1, dist, picked, cnt, ans)
	
	return ans
		

def main():
	n, m = map(int, input().split())
	points = [[-1, -1] for _ in range(n)]
	
	for i in range(n):
		points[i] = list(map(int, input().split()))
		
	print(pick(points, n, m, 0, 0, [], 0, INF))


if __name__ == "__main__":
	main()