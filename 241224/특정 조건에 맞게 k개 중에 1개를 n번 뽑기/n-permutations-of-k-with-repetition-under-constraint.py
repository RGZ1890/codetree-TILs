def solution(K, N, i, res):
    if i == N:
        print(*res)
        return
    for j in range(1, K + 1):
        if i >= 2 and res[i - 1] == res[i - 2] == j:
            continue
        solution(K, N, i + 1, res + [j])
    

def main():
    K, N = map(int, input().split())
    solution(K, N, 0, [])


if __name__ == "__main__":
    main()