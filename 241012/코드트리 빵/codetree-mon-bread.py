from collections import deque

dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def bfs(start, end):
    q = deque()
    q.append(start)
    visited = [[[] for _ in range(n)] for _ in range(n)]

    while q:
        cur = q.popleft()
        if cur == end:
            path = []
            while True:
                if cur == start:
                    return path[::-1]
                path.append(cur)
                cur = visited[cur[0]][cur[1]]
        for dir in dirs:
            nex = [cur[0] + dir[0], cur[1] + dir[1]]
            if not (0 <= nex[0] < n and 0 <= nex[1] < n):
                continue
            if not visited[nex[0]][nex[1]] and board[nex[0]][nex[1]] >= 0:
                visited[nex[0]][nex[1]] = cur
                q.append(nex)

    return []

def move_camp(p_pos, i):
    dist = 226  # 15 ** 2 + 1
    camp = [-1, -1]
    for c in camps:
        if board[c[0]][c[1]] != -1:
            path = bfs(cvs[i], c)
            if path and len(path) < dist:
                dist = min(dist, len(path))
                camp = c
    p_pos[i] = camp
    board[p_pos[i][0]][p_pos[i][1]] = -1

# 1 for camp, 2 for cvs

n, m = map(int, input().split())
board = [[0] * n for _ in range(n)]
p_board = [[0] * n for _ in range(n)]
p_pos = [[0, 0] for _ in range(m)]
cvs = [[0, 0] for _ in range(m)]
camps = []

for i in range(n):
    board[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            camps.append([i, j])

for i in range(m):
    cvs[i] = list(map(int, input().split()))
    cvs[i][0], cvs[i][1] = cvs[i][0] - 1, cvs[i][1] - 1

t = 0

while True:
    over = True


    for i in range(min(t, m)):
        if p_pos[i] == cvs[i]:
            continue
        path = bfs(p_pos[i], cvs[i])
        p_pos[i] = path[0]

    for i in range(m):
        if p_pos[i] == cvs[i]:
            board[cvs[i][0]][cvs[i][1]] = -1

    if t < m:
        move_camp(p_pos, t)
        
    for c in cvs:
        if board[c[0]][c[1]] != -1:
            over = False
            break
    if over:
        break
    t += 1

print(t + 1)