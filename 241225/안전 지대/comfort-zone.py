import sys
sys.setrecursionlimit(2501)

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(tmp_board, N, M, visited, K, cur):
    for d in dirs:
        next_pos = [cur[0] + d[0], cur[1] + d[1]]
        if tmp_board[next_pos[0]][next_pos[1]] > K\
        and not visited[next_pos[0]][next_pos[1]]:
            visited[next_pos[0]][next_pos[1]] = True
            visited = dfs(tmp_board, N, M, visited, K, next_pos)
    
    return visited


def solution(board, N, M, thres):
    ans_k, ans_cnt = -1, -1
    for K in range(1, thres + 1):
        visited = [[True] + [False] * M + [True] for _ in range(N + 2)]
        visited[0], visited[N + 1] = [True] * (M + 2), [True] * (M + 2)
        cnt = 0
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                if board[i][j] > K and not visited[i][j]:
                    visited[i][j] = True
                    cnt += 1
                    visited = dfs(board, N, M, visited, K, [i, j])
#       print("RES", K, cnt)
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