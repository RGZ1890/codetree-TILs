from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def bfs(board, n, start):
    dist = [[-2] * (n + 2) for _ in range(n + 2)]
    dist[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    
    while q:
        cur = q.popleft()
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if board[nex[0]][nex[1]] == 1 \
            and dist[nex[0]][nex[1]] == -2:
                dist[nex[0]][nex[1]] = dist[cur[0]][cur[1]] + 1
                q.append(nex)
            elif board[nex[0]][nex[1]] == 2:
                return dist[cur[0]][cur[1]] + 1
            
    return -2


def solution(board, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] == 0:
                print(-1, end = ' ')
            elif board[i][j] == 2:
                print(0, end = ' ')
            else:
                print(bfs(board, n, [i, j]), end = ' ')
        print()
    

def main():
    n, k = map(int, input().split())
    board = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        board[i] = [0] + list(map(int, input().split())) + [0]
    solution(board, n)
    

if __name__ == "__main__":
    main()