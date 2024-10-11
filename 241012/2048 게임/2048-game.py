def find_max(board, n):
    ref, cnt = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > ref:
                ref = board[i][j]
                cnt = 1
            elif board[i][j] == ref:
                cnt += 1

    return ref, cnt

def merge_board(cur_board, n):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if cur_board[i][j] != 0:
                for k in range(j - 1, -1, -1):
                    if cur_board[i][k] != 0:
                        if cur_board[i][k] != cur_board[i][j]:
                            break
                        else:
                            cur_board[i][j] *= 2
                            cur_board[i][k] = 0
                            break

    return cur_board

def move_board(cur_board, n):
    for i in range(n):
        for j in range(n - 1, 0, -1):
            if cur_board[i][j] == 0:
                for k in range(j - 1, -1, -1):
                    if cur_board[i][k] != 0:
                        cur_board[i][j], cur_board[i][k] = cur_board[i][k], cur_board[i][j]
                        break

    return cur_board


def change_board(board, n):
    pass
    # merge row or columns
    boards = [
        [[board[i][j] for i in range(n)] for j in range(n)],            # d
        [[board[n - i - 1][j] for i in range(n)] for j in range(n)],    # u
        [[board[i][n - j - 1] for j in range(n)] for i in range(n)],    # l
        [[board[i][j] for j in range(n)] for i in range(n)]             # r
    ]
    for i in range(4):
        boards[i] = merge_board(boards[i], n)
        boards[i] = move_board(boards[i], n)

    boards[0] = [[boards[0][i][j] for i in range(n)] for j in range(n)]
    boards[1] = [[boards[1][i][n - j - 1] for i in range(n)] for j in range(n)]
    boards[2] = [[boards[2][i][n - j - 1] for j in range(n)] for i in range(n)]

    return boards


def recursive_board(cur_board, n, turn):
    res = []
    if turn == 5:
        return find_max(cur_board, n)
    next_boards = change_board(cur_board, n)
    for i in range(4):
        res.append(recursive_board(next_boards[i], n, turn + 1))
    return max(res, key = lambda x: x[0])

n = int(input())
board = [[0] * n for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

ref, cnt = find_max(board, n)
best_board = [row[:] for row in board]


res = recursive_board(best_board, n, 0)
print(res[0])

# print(ref)