
def solution(n, cnt, picked, visited):
    if cnt == n:
        print(*picked)
        return
    
    for i in range(n, 0, -1):
        if visited[i] == False:
            visited[i] = True
            solution(n, cnt + 1, picked + [i], visited)
            visited[i] = False


def main():
    n = int(input())
    visited = [False] * (n + 1)
    solution(n, 0, [], visited)
    
    
if __name__ == "__main__":
    main()