import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * n for _ in range(m)]
answer = 0

for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().split()))

def Lshaped(board, res):
    for i in range(1, n):
        for j in range(1, n):
            subList = [board[i - 1][j - 1], board[i - 1][j],\
                        board[i][j - 1], board[i][j]]
            s = sum(subList) - min(subList)
            res = max(s, res)
    return res

def Ishaped(board, res):
    for row in board:
        for j in range(n - 3):
            res = max(sum(row[j:j + 3]), res)
    for i in range(n):
        col = [board[i][j] for j in range(n)]
        for j in range(n - 3):
            res = max(sum(row[j:j + 3]), res)
    return res

answer = Lshaped(board, answer)
answer = Ishaped(board, answer)
print(answer)