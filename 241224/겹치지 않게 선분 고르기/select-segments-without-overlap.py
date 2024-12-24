
def solution(lines, i, n, l_range, picked):
    if i == n:
        return len(picked)
    
    cnt = solution(lines, i + 1, n, l_range, picked)
    if lines[i][1] < l_range[0] or l_range[1] < lines[i][0] \
    or l_range[0] > l_range[1]:
        l_range = [min(l_range[0], lines[i][0]), max(l_range[1], lines[i][1])]
        cnt = max(cnt, solution(lines, i + 1, n, l_range, picked + [lines[i]]))
        
    return cnt
    

def main():
    n = int(input())
    lines = [[0, 0] for _ in range(n)]
    l_range = [1001, 0]
    for i in range(n):
        lines[i] = list(map(int, input().split()))

    cnt = solution(sorted(lines), 0, n, l_range, [])
    print(cnt)
    

if __name__ == "__main__":
    main()