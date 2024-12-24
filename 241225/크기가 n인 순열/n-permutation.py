def choose(n, cur, ans):
    if cur == n + 1:
        print(*ans)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        ans.append(i)
        choose(n, cur + 1, ans)
        ans.pop()
        visited[i] = False


n = int(input())

visited = [False] * (n + 1)
ans = []

choose(n, 1, ans)