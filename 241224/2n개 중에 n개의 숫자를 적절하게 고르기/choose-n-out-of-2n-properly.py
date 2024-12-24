INF = 10000


def pick(nums, n, cur, diff, cnt, ans):
	if cnt > n:
		return ans
	
	if cur == n * 2:
		return min(abs(diff), ans) if cnt == n else ans
	
	ans = pick(nums, n, cur + 1, diff + nums[cur], cnt + 1, ans)
	ans = pick(nums, n, cur + 1, diff - nums[cur], cnt, ans)
	
	return ans


def main():
	n = int(input())
	nums = list(map(int, input().split()))
	
	print(pick(nums, n, 0, 0, 0, INF))


if __name__ == "__main__":
	main()