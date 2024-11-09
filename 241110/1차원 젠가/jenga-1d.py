import sys

def moveBlock(block, s, e):
	l = len(block)
	tmp = [0] * (l - (e - s + 1))
	j = 0
	for i in range(l):
		if not s - 1 <= i <= e - 1:
			tmp[j] = block[i]
			j += 1
	
	return tmp


def main():
	n = int(input())
	block = [0] * n
	for i in range(n):
		block[i] = int(input())
	
	s1, e1 = map(int, input().split())
	s2, e2 = map(int, input().split())
	
	block = moveBlock(block, s1, e1)
	block = moveBlock(block, s2, e2)
	
	print(len(block))
	for cell in block:
		print(cell)
	

if __name__ == "__main__":
	main()