
def solution(adj_list, N, visited, cur, ans):
    for adj in adj_list[cur]:
        if not visited[adj]:
            visited[adj] = True
            ans = solution(adj_list, N, visited, adj, ans + 1)
            
    return ans


def main():
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N)]
    visited = [True] + [False] * (N - 1)
    for i in range(M):
        x, y = map(int, input().split())
        adj_list[x - 1].append(y - 1)
        adj_list[y - 1].append(x - 1)
    
    ans = solution(adj_list, N, visited, 0, 0)
    print(ans)
    
    
if __name__ == "__main__":
    main()