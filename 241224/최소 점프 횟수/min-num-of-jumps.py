INF = 999

def solution(nums, n, idx, ans, res):
#	print("IDX", idx, "VAL", nums[idx])
	if idx == n - 1:
		return res
	if res >= ans or idx > n - 1 or nums[idx] == 0:
		return INF
	
	for i in range(nums[idx], 0, -1):
		ans = min(ans, solution(nums, n, idx + i, ans, res + 1))
		
	return ans


def main():
	n = int(input())
	nums = list(map(int, input().split()))
	
	ans = solution(nums, n, 0, INF, 0)
	print(ans if ans != INF else -1)
	

if __name__ == "__main__":
	main()