from collections import deque

def cnt_turret(board, N, M):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                cnt += 1
            if cnt > 1:
                return 2
    return cnt

def find_turret(board, N, M, recency): #Flag: 0 for weak, 1 for strong
    cand_w, cand_s = [], []
    thres_w, thres_s = 50000, 0
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                if board[i][j] < thres_w:
                    thres_w = board[i][j]
                    cand_w = [[i, j]]
                elif board[i][j] == thres_w:
                    cand_w.append([i, j])
                if board[i][j] == thres_s:
                    cand_s.append([i, j])
                elif board[i][j] > thres_s:
                    thres_s = board[i][j]
                    cand_s = [[i, j]]

    # Round 2 - Recency
    if len(cand_w) != 1:
        cand_w2 = []
        thres_w = 0
        for c in cand_w:
            if recency[c[0]][c[1]] > thres_w:
                thres_w = recency[c[0]][c[1]]
                cand_w2 = [c]
            elif recency[c[0]][c[1]] == thres_w:
                cand_w2.append(c)
        cand_w = cand_w2
    if len(cand_s) != 1:
        cand_s2 = []
        thres_s = 1001
        for c in cand_s:
            if recency[c[0]][c[1]] < thres_s:
                thres_s = recency[c[0]][c[1]]
                cand_s2 = [c]
            elif recency[c[0]][c[1]] == thres_s:
                cand_s2.append(c)
        cand_s = cand_s2

    # Round 3 - sum of coordinates
    if len(cand_w) != 1:
        cand_w3 = []
        thres_w = 0
        for c in cand_w:
            if sum(c) > thres_w:
                thres_w = sum(c)
                cand_w3 = [c]
            elif sum(c) == thres_w:
                cand_w3.append(c)
        cand_w = cand_w3
    if len(cand_s) != 1:
        cand_s3 = []
        thres_s = 21
        for c in cand_s:
            if sum(c) < thres_s:
                thres_s = sum(c)
                cand_s3 = [c]
            elif sum(c) == thres_s:
                cand_s3.append(c)
        cand_s = cand_s3

    # Round 4 - Column coordinate
    if len(cand_w) != 1:
        cand_w4 = []
        thres_w = 0
        for c in cand_w:
            if c[1] > thres_w:
                thres_w = c[1]
                cand_w4 = [c]
        cand_w = cand_w4
    if len(cand_s) != 1:
        cand_s4 = []
        thres_s = 11
        for c in cand_s:
            if c[1] < thres_s:
                thres_s = c[1]
                cand_s4 = [c]
        cand_s = cand_s4

    return cand_w[0], cand_s[0]

def outbound(N, M, pos):
    pos[0] = N - 1 if pos[0] < 0 else pos[0]
    pos[0] = 0 if pos[0] == N else pos[0]
    pos[1] = M - 1 if pos[1] < 0 else pos[1]
    pos[1] = 0 if pos[1] == M else pos[1]

    return pos

# def BFS(board, N, M, laser_dir, pos, tgt, path, thres):
#     if pos == tgt:
#         path.append(pos)
#         return path, len(path)
#     if board[pos[0]][pos[1]] <= 0 or pos in path:
#         return path, thres
#     path.append(pos)
#     for i in range(4):
#         next_pos = [pos[0] + laser_dir[i][0], pos[1] + laser_dir[i][1]]
#         next_pos = outbound(N, M, next_pos)
#         next_path, next_dist = BFS(board, N, M, laser_dir, next_pos, tgt, path, thres)
#         if next_dist < thres:
#             return next_path, next_dist
#     return path, thres
#
# from collections import deque

def BFS(board, N, M, laser_dir, start, tgt, thres):
    queue = deque([(start, [start])])
    visited = set()
    visited.add(tuple(start))

    while queue:
        pos, path = queue.popleft()
        if pos == tgt:
            return path, len(path)
        for i in range(4):
            next_pos = [pos[0] + laser_dir[i][0], pos[1] + laser_dir[i][1]]
            next_pos = outbound(N, M, next_pos)
            if board[next_pos[0]][next_pos[1]] > 0 and tuple(next_pos) not in visited:
                visited.add(tuple(next_pos))
                queue.append((next_pos, path + [next_pos]))
    # If no path is found, return thres
    return [], thres

def laser_atk(board, laser_dir, N, M, attacker, tgt):
    pos = attacker
    splash = board[attacker[0]][attacker[1]] // 2
    cur_path, cur_dist = BFS(board, N, M, laser_dir, pos, tgt, 1000)

    if cur_dist < 1000:
        for i in range(1, cur_dist - 1):
            tur = cur_path[i]
            board[tur[0]][tur[1]] -= splash
        board[tgt[0]][tgt[1]] -= board[attacker[0]][attacker[1]]

    return cur_path

def art_atk(board, N, M, attacker, tgt):
    splash = board[attacker[0]][attacker[1]] // 2
    alt_tgt = []
    for dir in ([-1, 0], [-1, 1], [0, 1], [1, 1],
                [1, 0], [1, -1], [0, -1], [-1, -1]):
        tmp = [tgt[0] + dir[0], tgt[1] + dir[1]]
        tmp = outbound(N, M, tmp)
        if board[tmp[0]][tmp[1]] > 0 and tmp != attacker and tmp != tgt:
            alt_tgt.append(tmp)

    for t in alt_tgt:
        board[t[0]][t[1]] -= splash

    board[tgt[0]][tgt[1]] -= board[attacker[0]][attacker[1]]
    alt_tgt.append(tgt)
    return alt_tgt


laser_dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
N, M, K = map(int, input().split())
board = [[0] * N for _ in range(N)]
recency = [[0] * N for _ in range(N)]
bonus = N + M
for i in range(N):
    board[i] = list(map(int, input().split()))

for turn in range(1, K + 1):
    # print("----------------------------------\nTURN", turn)
    if cnt_turret(board, N, M) <= 1:
        # print("OVER")
        break
    attacker, target = find_turret(board, N, M, recency)
    # print("ATK", attacker, "TGT", target)
    board[attacker[0]][attacker[1]] += bonus
    recency[attacker[0]][attacker[1]] = turn

    res = laser_atk(board, laser_dir, N, M, attacker, target)
    # print("RES", res)
    if not res:
        res = art_atk(board, N, M, attacker, target)
    # print("RES", res)
    for i in range(N):
        for j in range(M):
            if board[i][j] > 0 and [i, j] not in res and [i, j] != attacker:
                board[i][j] += 1

    # for row in board:
        # print(row)

ans = 0
for i in range(N):
    for j in range(M):
        ans = max(ans, board[i][j])
print(ans)