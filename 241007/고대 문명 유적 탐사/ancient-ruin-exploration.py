def rotate(board, r, c): # Rotate 90'
    new_board = [x[:] for x in board]
    for i in range(3):
        for j in range(3):
            new_board[r + i][c + j] = board[r + 3 - j - 1][c + i]
    return new_board

def BFS(board, visited, i, j, is_clear):
    q = []
    cnt = 0
    pos = set()
    q.append((i, j))
    pos.add((i, j))
    visited[i][j] = 1
    cnt += 1

    while q:
        crow, ccol = q.pop(0)
        for dir in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            nrow, ncol = crow + dir[0], ccol + dir[1]
            if 0 <= nrow < 5 and 0 <= ncol < 5 \
                    and visited[nrow][ncol] == 0 \
                    and board[crow][ccol] == board[nrow][ncol]:
                q.append((nrow, ncol))
                visited[nrow][ncol] = 1
                pos.add((nrow, ncol))
                cnt += 1
    if cnt >= 3:
        if is_clear:
            for r, c in pos:
                board[r][c] = 0
        return cnt

    return 0

def count_clear(board, is_clear):
    visited = [[0] * 5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if visited[i][j] == 0:
                cnt += BFS(board, visited, i, j, is_clear)
    return cnt

K, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(5)]
wall = list(map(int, input().split()))
ans = []

for _ in range(K):
    max_cnt = 0
    max_board = [x[:] for x in board]
    for deg in range(1, 4):
        for j in range(3):
            for i in range(3):
                new_board = [x[:] for x in board]
                for _ in range(deg):
                    new_board = rotate(new_board, j, i)

                tmp = count_clear(new_board, False)
                if max_cnt < tmp:
                    max_cnt = tmp
                    max_board = new_board
    if max_cnt == 0:
        break

    cnt = 0
    board = max_board
    while True:
        tmp = count_clear(board, True)
        if tmp == 0:
            break
        cnt += tmp
        for j in range(5):
            for i in range(4, -1, -1):
                if board[i][j] == 0:
                    board[i][j] = wall.pop(0)
    ans.append(cnt)

print(*ans)