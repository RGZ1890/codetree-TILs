from collections import deque
import sys

sys.setrecursionlimit(8 ** 8)

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(board, n, s, avail):
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
                
    return avail


def solution(board, n, starts, rocks, lr, r_cnt, ans):
#   print("RCNT", r_cnt, ans)
    if r_cnt == lr:
        avail = set()
        for s in starts:
            avail = bfs(board, n, s, avail)
        return max(ans, len(avail))
    
    for r in rocks:
        if board[r[0]][r[1]] == 1:
            board[r[0]][r[1]] = 0
            ans = solution(board, n, starts, rocks, lr, r_cnt + 1, ans)
            board[r[0]][r[1]] = 1
    
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
    
    if len(rocks) <= m:
        for r in rocks:
            board[r[0]][r[1]] = 0
        m = 0
    print(solution(board, n, starts, rocks, min(len(rocks), m), 0, 0))
        
        
if __name__ == "__main__":
    main()
        