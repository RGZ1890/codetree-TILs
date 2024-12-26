from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(board, n, m):
    start, end = [1, 1], [n, m]
    visited = [[False] * (m + 2) for _ in range(n + 2)]
    visited[start[0]][start[1]] = True
    q = deque()
    q.append(start)
    
    while q:
        cur = q.popleft()
        if cur == end:
            return 1
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if not visited[nex[0]][nex[1]] \
            and board[nex[0]][nex[1]] == 1:
                visited[nex[0]][nex[1]] = True
                q.append(nex)
                
    return 0


def main():
    n, m = map(int, input().split())
    board = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        tmp = list(map(int, input().split()))
        board[i] = [0] + tmp + [0]
    
    print(bfs(board, n, m))
    
    
if __name__ == "__main__":
    main()