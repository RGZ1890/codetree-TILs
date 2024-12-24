dirs = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def solution(board, n, cur, cnt, ans):
#   print("CUR", cur, "CNT", cnt, "ANS", ans)
    cdir = dirs[board[cur[0]][cur[1]][1]]
    cval = board[cur[0]][cur[1]][0]
    
    for i in range(n):
        npos = [cur[0] + cdir[0] * i, cur[1] + cdir[1] * i]
        if 0 <= npos[0] < n and 0 <= npos[1] < n:
            if board[npos[0]][npos[1]][0] > cval:
                ans = solution(board, n, npos, cnt + 1, ans)
        else:
            break
        
    return max(cnt, ans)


def main():
    n = int(input())
    board = [[[0, 0] for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        ns = list(map(int, input().split()))
        for j in range(n):
            board[i][j][0] = ns[j]
    for i in range(n):
        ds = list(map(int, input().split()))
        for j in range(n):
            board[i][j][1] = ds[j] - 1
    
    start = list(map(int, input().split()))
    start = [start[0] - 1, start[1] - 1]
    
    answer = solution(board, n, start, 0, 0)
    print(answer)
        

if __name__ == "__main__":
    main()