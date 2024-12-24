
def solution(n, res, ans):
	if len(res) == n:
#		print(res)
		return ans + 1
	elif len(res) > n:
		return ans
	
	for i in range(1, 5):
		ans = solution(n, res + str(i) * i, ans)
	
	return ans
		

def main():
	n = int(input())
	ans = solution(n, '', 0)
	print(ans)
	

if __name__ == "__main__":
	main()