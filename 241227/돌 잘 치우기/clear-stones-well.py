from collections import deque
import sys

sys.setrecursionlimit(8 ** 8)

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(board, n, s, rock, avail):
    for r in rock:
        board[r[0]][r[1]] = 0
        
    visited = [[False] * n for _ in range(n)]
    visited[s[0]][s[1]] = True
    q = deque()
    q.append(s)
    
    while q:
        cur = q.popleft()
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if 0 <= nex[0] < n and 0 <= nex[1] < n \
            and board[nex[0]][nex[1]] == 0 \
            and not visited[nex[0]][nex[1]]:
                visited[nex[0]][nex[1]] = True
                avail.add((nex[0], nex[1]))
                q.append(nex)
    
    for r in rock:
        board[r[0]][r[1]] = 1
                
    return avail


def pick_rock(picked, cur, m, lr, res):
    if cur == lr:
        if len(picked) == m:
            return res + [picked]
        return res
    
    res = pick_rock(picked + [cur], cur + 1, m, lr, res)
    res = pick_rock(picked, cur + 1, m, lr, res)
    
    return res


def solution(board, n, starts, m, rocks):
    ans = 0
    lr = len(rocks)
    res = pick_rock([], 0, m, lr, [])
#   print("RES", res)
    for pick in res:
        rock = [rocks[p] for p in pick]
        avail = set()
        for s in starts:
            avail.add((s[0], s[1]))
            avail = bfs(board, n, s, rock, avail)
        cnt = len(avail)
        if cnt == n ** 2 - lr + m:
            return cnt
        ans = max(ans, cnt)
        
    return ans


def main():
    n, k, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    starts = [[0, 0] for _ in range(k)]
    rocks = []
    for i in range(n):
        board[i] = list(map(int, input().split()))
        for j in range(n):
            if board[i][j] == 1:
                rocks.append([i, j])
    
    for i in range(k):
        r, c = map(int, input().split())
        starts[i] = [r - 1, c - 1]
    
    print(solution(board, n, starts, m, rocks))
    
        
if __name__ == "__main__":
    main()
        