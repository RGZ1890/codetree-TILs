def xor(res, m):
	ret = res[0]
	for i in range(1, m):
		ret ^= res[i]
	
	return ret


def pick(n, m, nums, cur, res, ans):
	if len(res) == m:
#		print(res, xor(res, m))
		return max(ans, xor(res, m))
	
	if cur > n - 1:
		return -1
	
	ans = max(pick(n, m, nums, cur + 1, res + [nums[cur]], ans),
			pick(n, m, nums, cur + 1, res, ans))
	
	return ans
	

def main():
	n, m = map(int, input().split())
	nums = list(map(int, input().split()))
	
	ans = pick(n, m, nums, 0, [], -1)
	print(ans)
	

if __name__ == "__main__":
	main()