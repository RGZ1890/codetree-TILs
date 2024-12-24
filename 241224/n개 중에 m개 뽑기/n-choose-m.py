
def solution(N, M, cur, res):
	if len(res) == M:
		print(*res)
		return
	if cur > N:
		return
	
	res.append(cur)
	solution(N, M, cur + 1, res)
	res.pop()
	solution(N, M, cur + 1, res)


def main():
	N, M = map(int, input().split())
	
	solution(N, M, 1, [])
	

if __name__ == "__main__":
	main()