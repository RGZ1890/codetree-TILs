from collections import deque

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def bfs(board, visited, s, ans):
    q = deque()
    q.append(s)
    
    while q:
        cur = q.popleft()
        ans += 1
        for d in dirs:
            nex = [cur[0] + d[0], cur[1] + d[1]]
            if not visited[nex[0]][nex[1]] \
            and board[nex[0]][nex[1]] == 0:
                visited[nex[0]][nex[1]] = True
                q.append(nex)
    
    return visited, ans
    


def solution(board, n, starts):
    visited = [[False] * (n + 2) for _ in range(n + 2)]
    ans = 0
    for s in starts:
        if not visited[s[0]][s[1]]:
            visited[s[0]][s[1]] = True
            visited, ans = bfs(board, visited, s, ans)
    
    return ans


def main():
    n, k = map(int, input().split())
    board = [[1] * (n + 2) for _ in range(n + 2)]
    starts = [[0, 0] for _ in range(k)]
    for i in range(1, n + 1):
        board[i] = [1] + list(map(int, input().split())) + [1]
    for i in range(k):
        starts[i] = list(map(int, input().split()))
    
    print(solution(board, n, starts))
    

if __name__ == "__main__":
    main()