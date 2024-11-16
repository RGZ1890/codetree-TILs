dirs = {'L': [0, -1], 'R': [0, 1], 'U': [-1, 0], 'D': [1, 0]}
top, front, right = 0, 1, 2

def rolldice(dice, comm):
	if comm == 'L':
		dice[top], dice[front], dice[right] = dice[right], dice[front], dice[top][::-1]
	elif comm == 'R':
		dice[top], dice[front], dice[right] = dice[right][::-1], dice[front], dice[top]
	elif comm == 'U':
		dice[top], dice[front], dice[right] = dice[front], dice[top][::-1], dice[right]
	else:
		dice[top], dice[front], dice[right] = dice[front][::-1], dice[top], dice[right]
		
	return dice


def main():
	n, m, r, c = map(int, input().split())
	board = [[0] * n for _ in range(n)]
	cur = [r - 1, c - 1]
	dice = [[1, 6], [2, 5], [3, 4]]
	comms = input().split()
	board[cur[0]][cur[1]] = dice[0][1]
	
	for c in comms:
		nex = [cur[0] + dirs[c][0], cur[1] + dirs[c][1]]
		if 0 <= nex[0] < n and 0 <= nex[1] < n:
			cur = nex
			dice = rolldice(dice, c)
			board[cur[0]][cur[1]] = dice[0][1]
		
#		print("===============")
#		for row in board:
#			print(*row)
	
	answer = 0
	for row in board:
		answer += sum(row)
	print(answer)


if __name__ == "__main__":
	main()