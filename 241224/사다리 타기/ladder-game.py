INF = 16


def walk(n, lines):
    cur = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        for l in lines:
            if cur[i] == l[0]:
                cur[i] = l[1]
            elif cur[i] == l[1]:
                cur[i] = l[0]
                
    return cur[1:]


def solution(n, m, res, lines, i, picked, cur, ans):
    if cur >= ans:
        return INF
    if i == m:
        if walk(n, picked) == res:
            return cur
        return ans
    
    return min(solution(n, m, res, lines, i + 1, picked, cur, ans),
        solution(n, m, res, lines, i + 1, picked + [lines[i]], cur + 1, ans))


def main():
    n, m = map(int, input().split())
    lines = [[0, 0, 0] for _ in range(m)]
    for i in range(0, m):
        a, b = map(int, input().split())
        lines[i] = [a, a + 1, b]
    
    lines = sorted(lines, key = lambda x: x[2])
    res = walk(n, lines)
    ans = solution(n, m, res, lines, 0, [], 0, INF)
    print(ans)


if __name__ == "__main__":
    main()