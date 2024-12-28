from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(board, n, start, end):
    dist = [[n * n] * (n + 2) for _ in range(n + 2)]
    dist[start[0]][start[1]] = 0
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if board[nex[0]][nex[1]] == 0 \
            and dist[nex[0]][nex[1]] == n * n:
                dist[nex[0]][nex[1]] = dist[cur[0]][cur[1]] + 1
                if nex == end:
                    return dist[nex[0]][nex[1]]
                q.append(nex)
        
    return n * n


def pick(w, k, cur, picked, comb):
    if len(picked) == k:
        return comb + [picked]
    if cur == w:
        return comb
    
    comb = pick(w, k, cur + 1, picked + [cur], comb)
    comb = pick(w, k, cur + 1, picked, comb)
    
    return comb


def solution(board, n, walls, k, start, end):
    if start == end:
        return 0
    comb = pick(len(walls), k, 0, [], [])
    ans = n * n
    for c in comb:
        for w in c:
            board[walls[w][0]][walls[w][1]] = 0
        ans = min(ans, bfs(board, n, start, end))
        for w in c:
            board[walls[w][0]][walls[w][1]] = 1
            
    return ans if ans != n * n else -1
    

def main():
    n, k = map(int, input().split())
    board = [[1] * (n + 2) for _ in range(n + 2)]
    walls = []
    
    for i in range(1, n + 1):
        board[i] = [1] + list(map(int, input().split())) + [1]
        for j in range(1, n + 1):
            if board[i][j] == 1:
                walls.append([i, j])
    
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
        
    print(solution(board, n, walls, k, start, end))
    

if __name__ == "__main__":
    main()