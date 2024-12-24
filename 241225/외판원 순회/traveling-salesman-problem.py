INF = 200000

def solution(adj, n, visited, pos, cur, cnt, ans):
    if cur > ans or cnt > n:
        return ans
    
    if cnt == n and pos == 0:
        return min(ans, cur)
    
    for dest in range(n):
        if not visited[dest]:
            visited[dest] = True
            ans = solution(adj, n, visited, dest, cur + adj[pos][dest], cnt + 1, ans)
            visited[dest] = False
            
    return ans


def main():
    n = int(input())
    adj = [[0] * n for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        adj[i] = list(map(int, input().split()))
        for j in range(n):
            adj[i][j] = INF if adj[i][j] == 0 else adj[i][j]
    
    print(solution(adj, n, visited, 0, 0, 0, INF))
    

if __name__ == "__main__":
    main()