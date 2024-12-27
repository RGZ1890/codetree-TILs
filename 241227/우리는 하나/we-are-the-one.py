from collections import deque
dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def moveable(board, n, cur, nex, u, d):
    if 0 <= nex[0] < n and 0 <= nex[1] < n:
        diff = abs(board[cur[0]][cur[1]] - board[nex[0]][nex[1]])
        return u <= diff <= d
    return False


def bfs(board, n, visited, city, path, u, d):
    q = deque()
    q.append(city)
    
    while q:
        cur = q.popleft()
        path.add((cur[0], cur[1]))
        for di in dirs:
            nex = [cur[0] + di[0], cur[1] + di[1]]
            if moveable(board, n, cur, nex, u, d) \
            and not visited[nex[0]][nex[1]]:
                visited[nex[0]][nex[1]] = True
                q.append(nex)

    return path


def pick_city(cities, c, k, picked, cur, res):
    if len(picked) > k:
        return res
    if len(picked) == k:
        return res + [picked]
    if cur == c:
        return res

    res = pick_city(cities, c, k, picked + [cities[cur]], cur + 1, res)
    res = pick_city(cities, c, k, picked, cur + 1, res)
    
    return res


def solution(board, n, k, u, d):
    cities = []
    for i in range(n):
        for j in range(n):
            cities.append([i, j])
    res = pick_city(cities, n ** 2, k, [], 0, [])
    
    ans = 0
    for comb in res:
        path = set()
        visited = [[False] * n for _ in range(n)]
        for city in comb:
            if not visited[city[0]][city[1]]:
                visited[city[0]][city[1]] = True
                path = bfs(board, n, visited, city, path, u, d)
        
        ans = max(ans, len(path))
        if ans == n ** 2:
            return ans
    
    return ans


def main():
    n, k, u, d = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().split()))
    
    print(solution(board, n, k, u, d))
    

if __name__ == "__main__":
    main()
    
    
    