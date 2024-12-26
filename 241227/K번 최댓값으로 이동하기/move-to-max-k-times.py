from collections import deque

dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]

def bfs(board, n, cur):
    visited = [[False] * (n + 2) for _ in range(n + 2)]
    visited[cur[0]][cur[1]] = True
    q = deque()
    q.append(cur)
    path = []
    val = board[cur[0]][cur[1]]
    val_max = 0
    
    while q:
        cur = q.popleft()
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if board[nex[0]][nex[1]] < val \
            and not visited[nex[0]][nex[1]]:
                visited[nex[0]][nex[1]] = True
                q.append(nex)
                if val_max < board[nex[0]][nex[1]]:
                    path = [[nex[0], nex[1], board[nex[0]][nex[1]]]]
                    val_max = board[nex[0]][nex[1]]
                elif val_max == board[nex[0]][nex[1]]:
                    path.append([nex[0], nex[1], board[nex[0]][nex[1]]])
                    
    return path


def solution(board, n, start, k):
    cur = start
    for _ in range(k):
        path = bfs(board, n, cur)
        if not path:
            break
#       print("PATH", path)
            
        nex = [n, n]
        for p in path:
            if p[0] < nex[0] or p[0] == nex[0] and p[1] < nex[1]:
                nex = p
        cur = nex
        
    print(cur[0], cur[1])


def main():
    n, k = map(int, input().split())
    board = [[101] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        board[i] = [101] + list(map(int, input().split())) + [101]
    
    start = list(map(int, input().split()))
    
    solution(board, n, start, k)


if __name__ == "__main__":
    main()