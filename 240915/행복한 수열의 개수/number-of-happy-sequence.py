import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * n for _ in range(n)]

def HappyList(row, n, m):
    streak = 1
    for i in range(1, n):
        streak = streak + 1 if (row[i] == row[i - 1]) else 1
        if (streak == m):
            return 1
    return 0

answer = 0
if (n == 1) answer = 1
for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))
    answer += HappyList(board[i], n, m)
for j in range(n):
    row = [board[i][j] for i in range(n)]
    answer += HappyList(row, n, m)

print(answer)