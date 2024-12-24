INF = 200000

def solution(adj, n, visited, pos, cur, cnt, ans):
    if cur > ans:
        return ans
    
    if cnt == n:
#       print("DONE", min(ans, cur) if pos == 0 else ans)
        return min(ans, cur) if pos == 0 else ans
    
    for dest in range(n):
        if not visited[dest] and adj[pos][dest] != 0:
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
    
    print(solution(adj, n, visited, 0, 0, 0, INF))
    

if __name__ == "__main__":
    main()