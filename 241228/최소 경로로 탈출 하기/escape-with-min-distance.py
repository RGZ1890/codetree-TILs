from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(board, n, m):
    visited = [[False] * (m + 2) for _ in range(n + 2)]
    step = [[n * m] * (m + 2) for _ in range(n + 2)]
    step[1][1] = 0
    visited[1][1] = True
    q = deque()
    q.append([1, 1])
    
    while q:
        cur = q.popleft()
        if cur == [n, m]:
            return step[n][m]
        
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if board[nex[0]][nex[1]] == 1 \
            and not visited[nex[0]][nex[1]]:
                visited[nex[0]][nex[1]] == True
                step[nex[0]][nex[1]] = min(step[cur[0]][cur[1]] + 1, step[nex[0]][nex[1]])
                q.append(nex)
    
    return -1


def main():
    n, m = map(int, input().split())
    board = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        tmp = list(map(int, input().split()))
        board[i] = [0] + tmp + [0]
    
    print(bfs(board, n, m))


if __name__ == "__main__":
    main()