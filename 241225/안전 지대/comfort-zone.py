import sys
sys.setrecursionlimit(2501)

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(tmp_board, N, M, visited, K, cur):
    for d in dirs:
        next_pos = [cur[0] + d[0], cur[1] + d[1]]
        if 0 <= next_pos[0] < N and 0 <= next_pos[1] < M \
        and tmp_board[next_pos[0]][next_pos[1]] > K \
        and not visited[next_pos[0]][next_pos[1]]:
            visited[next_pos[0]][next_pos[1]] = True
            visited = dfs(tmp_board, N, M, visited, K, next_pos)
    
    return visited


def solution(board, N, M, possible_k):
    ans_k, ans_cnt = -1, -1
    for K in possible_k:
        visited = [[False] * M for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(M):
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
    board = [[0] * M for _ in range(N)]
    possible_k = set()
    
    for i in range(N):
        tmp = list(map(int, input().split()))
        board[i] = tmp
        for t in tmp:
            possible_k.add(t)
    
    solution(board, N, M, possible_k)
    

if __name__ == "__main__":
    main()