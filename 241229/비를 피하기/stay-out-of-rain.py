from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(board, n, s):
    dist = [[n * n] * n for _ in range(n)]
    dist[s[0]][s[1]] = 0
    q = deque()
    q.append(s)
    
    while q:
        cur = q.popleft()
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if 0 <= nex[0] < n and 0 <= nex[1] < n \
            and board[nex[0]][nex[1]] != 1 \
            and dist[nex[0]][nex[1]] == n * n:
                dist[nex[0]][nex[1]] = dist[cur[0]][cur[1]] + 1
                if board[nex[0]][nex[1]] == 3:
                    return dist[nex[0]][nex[1]]
                q.append(nex)
        
    return -1


def solution(board, n):
    for i in range(n):
        for j in range(n):
            print(bfs(board, n, [i, j]) if board[i][j] == 2 else 0, end = ' ')
        print()


def main():
    n, h, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().split()))
    
    solution(board, n)
        
        
if __name__ == "__main__":
    main()
        