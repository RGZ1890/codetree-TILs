dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(tmp_board, N, M, visited, K, cur):
    for d in dirs:
        next_pos = [cur[0] + d[0], cur[1] + d[1]]
        if 0 <= next_pos[0] < N and 0 <= next_pos[1] < M \
        and tmp_board[next_pos[0]][next_pos[1]]\
        and not visited[next_pos[0]][next_pos[1]]:
            visited[next_pos[0]][next_pos[1]] = True
            visited = dfs(tmp_board, N, M, visited, K, next_pos)
    
    return visited


def solution(board, N, M, thres):
    ans_k, ans_cnt = -1, -1
    for K in range(1, thres + 1):
        tmp_board = [[True if cell > K else False for cell in row] for row in board]
        visited = [[False] * (M + 2) for _ in range(N + 2)]
        cnt = 0
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if tmp_board[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    cnt += 1
                    visited = dfs(tmp_board, N, M, visited, K, [i, j])
                    
        if cnt > ans_cnt:
            ans_k, ans_cnt = K, cnt
        
    print(ans_k, ans_cnt)


def main():
    N, M = map(int, input().split())
    board = [[0] * (M + 2) for _ in range(N + 2)]
    thres = 0
    
    for i in range(1, N + 1):
        tmp = list(map(int, input().split()))
        thres = max(thres, max(tmp))
        board[i] = [0] + tmp + [0]
        
    solution(board, N, M, thres)
    

if __name__ == "__main__":
    main()