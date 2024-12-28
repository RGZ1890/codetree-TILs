from collections import deque

def bfs(N):
    dist = [-1] * (N * 2)
    dist[N] = 0
    q = deque()
    q.append(N)
    
    while q:
        cur = q.popleft()
        if cur == 1:
            break
        
        nexdist = dist[cur] + 1
        if dist[cur - 1] == -1:
            dist[cur - 1] = nexdist
            q.append(cur - 1)
        if dist[cur + 1] == -1:
            dist[cur + 1] = nexdist
            q.append(cur + 1)
        if dist[cur // 2] == -1 \
        and cur % 2 == 0:
            dist[cur // 2] = nexdist
            q.append(cur // 2)
        if dist[cur // 3] == -1 \
        and cur % 3 == 0:
            dist[cur // 3] = nexdist
            q.append(cur // 3)
    
    return dist[1]
            

def main():
    N = int(input())
    print(bfs(N))
    

if __name__ == "__main__":
    main()