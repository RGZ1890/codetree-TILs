from collections import deque

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(board, n, m):
    start, end = (1, 1), (n, m)
    visited = [[False] * (m + 2) for _ in range(n + 2)]
    visited[start[0]][start[1]] = True
    q = deque([start])
    
    while q:
        cur_row, cur_col = q.popleft()
        if (cur_row, cur_col) == end:
            return 1
        for dr, dc in dirs:
            next_row, next_col = cur_row + dr, cur_col + dc
            if not visited[next_row][next_col] and board[next_row][next_col] == 1:
                visited[next_row][next_col] = True
                q.append((next_row, next_col))
                
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