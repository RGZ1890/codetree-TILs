dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(board, N, M, visited, K, cur):
    for d in dirs:
        next_pos = [cur[0] + d[0], cur[1] + d[1]]
        if 0 <= next_pos[0] < N and 0 <= next_pos[1] < M \
        and board[next_pos[0]][next_pos[1]] > K \
        and not visited[next_pos[0]][next_pos[1]]:
            visited[next_pos[0]][next_pos[1]] = True
            visited = dfs(board, N, M, visited, K, next_pos)
    
    return visited


def solution(board, N, M, thres):
    ans_k, ans_cnt = -1, -1
    for K in range(1, thres + 1):
        visited = [[False] * M for _ in range(N)]
        cnt = 0
        
        for i in range(N):
            for j in range(M):
                if board[i][j] > K and not visited[i][j]:
                    visited[i][j] = True
                    cnt += 1
                    visited = dfs(board, N, M, visited, K, [i, j])
        
        if cnt > ans_cnt:
            ans_k, ans_cnt = K, cnt
        
    print(ans_k, ans_cnt)


def main():
    N, M = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    thres = 0
    
    for i in range(N):
        board[i] = list(map(int, input().split()))
        thres = max(thres, max(tmp))
        
    solution(board, N, M, thres)
    

if __name__ == "__main__":
    main()