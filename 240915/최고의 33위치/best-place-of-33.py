import sys

N = int(sys.stdin.readline())

def curMax(board, r, c, answer):
    res = 0
    for i in range(r - 2, r + 1):
        for j in range(c - 2, c + 1):
            res += board[i][j]
    return res if (res > answer) else answer

board = [[0] * N for _ in range(N)]
answer = 0
for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().split()))
    if (i > 1):
        for j in range(2, N):
            answer = curMax(board, i, j, answer)

print(answer)