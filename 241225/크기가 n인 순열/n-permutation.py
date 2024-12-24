def choose(n, visited, cur, ans):
    if cur == n + 1:
        print(*ans)
        return

    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        choose(n, visited, cur + 1, ans + [i])
        visited[i] = False
        

def main():
    n = int(input())
    
    visited = [False] * (n + 1)
    choose(n, visited, 1, [])
    

if __name__ == "__main__":
    main()