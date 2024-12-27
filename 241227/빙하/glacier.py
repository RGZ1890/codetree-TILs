from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(board, N, M, start, visited, res):
    visited[start[0]][start[1]] = True
    q = deque()
    q.append(start)
    is_outer = False
    
    while q:
        cur = q.popleft()
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if 0 <= nex[0] < N and 0 <= nex[1] < M \
            and not visited[nex[0]][nex[1]]:
                if not is_outer:
                    is_outer = cur[0] == 0 or cur[0] == N \
                            or cur[1] == 0 or cur[1] == M
                elif board[nex[0]][nex[1]] == 1:
                    res.add((nex[0], nex[1]))
                if board[nex[0]][nex[1]] == 0:
                    visited[nex[0]][nex[1]] = True
                    q.append(nex)

    return res


def solution(board, N, M):
    ans, ans_cnt = 0, 0
    while True:
        ans += 1
        visited = [[False] * M for _ in range(N)]
        res = set()
        for i in range(N):
            for j in range(M):
                if not visited[i][j] and board[i][j] == 0:
                    res = bfs(board, N, M, [i, j], visited, res)
        if not res:
            ans -= 1
            break
#       print("RES", res, len(res))
        ans_cnt = len(res)
        for r in res:
            board[r[0]][r[1]] = 0
                
    return ans, ans_cnt
    


def main():
    N, M = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    
    for i in range(N):
        board[i] = list(map(int, input().split()))
        
    print(*solution(board, N, M))
    
    
if __name__ == "__main__":
    main()