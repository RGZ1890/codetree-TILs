import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))

def Lshaped(board, res, n, m):
    for i in range(1, n):
        for j in range(1, m):
            subList = [board[i - 1][j - 1], board[i - 1][j],\
                        board[i][j - 1], board[i][j]]
#           print(subList)
            s = sum(subList) - min(subList)
            res = max(s, res)
    return res

def vertical(board, res, n, m):
    for j in range(m):
        col = [board[i][j] for i in range(n)]
        for i in range(2, n):
#           print("col", col[i - 2:i + 1])
            res = max(sum(col[i - 2:i + 1]), res)
    return res

def horizontal(board, res, n, m):
    for i in range(n):
        row = board[i]
        for j in range(2, m):
#           print("row", row[j - 2:j + 1])
            res = max(sum(row[j - 2:j + 1]), res)
    return res

answer = Lshaped(board, answer, n, m)
answer = vertical(board, answer, n, m)
answer = horizontal(board, answer, n, m)

print(answer)