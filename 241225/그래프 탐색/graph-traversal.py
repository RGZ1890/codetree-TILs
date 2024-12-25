
def solution(adj_mat, N, visited, cur, ans):
    for i in range(N):
        if adj_mat[cur][i] and not visited[i]:
            visited[i] = True
            ans = solution(adj_mat, N, visited, i, ans + 1)
            
    return ans


def main():
    N, M = map(int, input().split())
    adj_mat = [[0] * N for _ in range(N)]
    visited = [True] + [False] * (N - 1)
    for i in range(M):
        x, y = map(int, input().split())
        adj_mat[x - 1][y - 1], adj_mat[y - 1][x - 1] = True, True
    
    ans = solution(adj_mat, N, visited, 0, 0)
    print(ans)
    
    
if __name__ == "__main__":
    main()