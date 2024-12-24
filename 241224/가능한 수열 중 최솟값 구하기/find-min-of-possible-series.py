def legit(s):
	ls = len(s)
	for l in range(1, ls // 2 + 1):
		for i in range(ls - l):
			if s[i:i + l] == s[i + l:i + l * 2]:
				return False
	return True


def sol(s, n):
#	print("s", s, "\tlegit", legit(s))
	if legit(s):
		if len(s) == n:
			return s
	
		for num in "456":
			t = sol(s + str(num), n)
			if t != "":
				return t
			
	return ""


def main():
	n = int(input())
	print(sol('', n))
	
	
if __name__ == "__main__":
	main()