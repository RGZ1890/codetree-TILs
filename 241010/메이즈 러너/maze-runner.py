def get_dist(A, B):
    return abs(A[0] - B[0]) + abs(A[1] - B[1])

def p_move(board, N, pos, out):
    # print("POS", pos)
    cur_pos = [p for p in pos]
    cur_dist = get_dist(cur_pos, out)
    # print("CUR_DIST", cur_dist, end = ' ')
    next_pos = [0, 0]
    dir = -1
    for i in range(4):
        next_pos[0] = pos[0] + directions[i][0]
        next_pos[1] = pos[1] + directions[i][1]
        # print("NEXT", next_pos)
        if 1 <= next_pos[0] <= N and 1 <= next_pos[1] <= N:
            # print("NEXT_VALID", next_pos, end = ' ')
            if board[next_pos[0]][next_pos[1]] == 0:
                next_dist = get_dist(next_pos, out)
                if next_dist < cur_dist:
                    # print("YES", end = ' ')
                    cur_pos = [next_pos[0], next_pos[1]]
                    cur_dist = next_dist
                    dir = i
            elif board[next_pos[0]][next_pos[1]] == -10:
                cur_pos = [0, 0]
                dir = -2
                break


    return cur_pos, dir

def find_subboard(participants, out, N, min_size):
    res_range = []
    for i in range(out[0], out[0] - min_size, -1):
        for j in range(out[1], out[1] - min_size, -1):
            if 1 <= i <= N - min_size and 1 <= j <= N - min_size:
                temp_range = [i, j, i + min_size, j + min_size]
                # print("RANGE_CAND", temp_range)
                found = False
                for r in range(temp_range[0], temp_range[2]):
                    for c in range(temp_range[1], temp_range[3]):
                        if [r, c] in participants:
                            found = True
                            res_range = temp_range
                            break
                    if found:
                        break

    return res_range

def rotate_board(board, participants, ranges, out, min_size):
    u, l, d, r = ranges
    # horizontal = [board[i] for i in range(u, d)]
    vertical = [[board[i][j] for i in range(u, d)] for j in range(l, r)]
    tgt = []

    for i in range(u, d):
        for j in range(l, r):
            for p in range(len(participants)):
                if participants[p] == [i, j]:
                    tgt.append(p)
            board[i][j] = vertical[i - u][r - j - 1]
            if board[i][j] == -10:
                out = [i, j]
            elif board[i][j] > 0:
                board[i][j] -= 1

    for p in tgt:
        # print("TGT", participants[p], end = ' ')
        r, c = participants[p][0] - u, participants[p][1] - l
        participants[p] = [u + c, l + min_size - 1 - r]
        # print(u, l, r, c, [c, min_size - 1 - r], "TGT_AFTER", participants[p])

    return board, out

N, M, K = map(int, input().split())
board = [[-1] * (N + 2) for _ in range(N + 2)]
participants = [[0, 0] for _ in range(M)]

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
moves = [0] * M

for i in range(1, N + 1):
    board[i] = [-1] + list(map(int, input().split())) + [-1]

for i in range(M):
    participants[i] = list(map(int, input().split()))

out = list(map(int, input().split()))
board[out[0]][out[1]] = -10


for _ in range(K):
    # print("-------------------\nOUT", out)
    min_size = 20
    is_over = True
    for i in range(1, M):
        if participants[i] != [0, 0]:
            is_over = False
            participants[i], dir = p_move(board, N, participants[i], out)
            moves[i] += 1 if dir != -1 else 0
            # print("POS_AFTER", i, participants[i])
            size_cand = max(abs(participants[i][0] - out[0]),
                            abs(participants[i][1] - out[1])) + 1
            min_size = min(min_size, size_cand)
    if is_over:
        break
    # print("PARTICIPANTS", participants)
    # print("MOVES", moves)
    # print("MIN_SIZE", min_size)
    ranges = find_subboard(participants, out, N, min_size)
    if ranges == []:
        break
    # print("RANGES", ranges)
    # print("BOARD_BEFORE")
    # for row in board:
        # print(row)
    board, out = rotate_board(board, participants, ranges, out, min_size)
    # print("BOARD_AFTER")
    # for row in board:
        # print(row)
    # print("POS_AFTER")
    # print(participants)


print(sum(moves))
print(*out)