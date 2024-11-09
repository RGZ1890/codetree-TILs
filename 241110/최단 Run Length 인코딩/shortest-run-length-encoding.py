def runLenEnc(s, l):
	res = ''
	ref = s[0]
	idx, cnt = 1, 1
	while idx < l:
		c = s[idx]
		if ref != c:
			res += ref + str(cnt)
			ref = c
			cnt = 1
		else:
			cnt += 1
		idx += 1
	res += ref + str(cnt)
	
	return res
	

def main():
	s = input()
	l = len(s)
	move = l
	while s[0] == s[move - 1] and move > 0:
		move -= 1
	s = s[move:] + s[:move]
	res = runLenEnc(s, l)
	print(len(res))
	

if __name__ == "__main__":
	main()