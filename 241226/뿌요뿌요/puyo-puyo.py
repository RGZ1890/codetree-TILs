dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(board, n, visited, cur, val, cnt):
    for d in dirs:
        nex = [cur[0] + d[0], cur[1] + d[1]]
        if 0 <= nex[0] < n and 0 <= nex[1] < n \
        and board[nex[0]][nex[1]] == val \
        and not visited[nex[0]][nex[1]]:
            visited[nex[0]][nex[1]] = True
            visited, cnt = dfs(board, n, visited, nex, val, cnt + 1)
            
    return visited, cnt


def solution(board, n):
    visited = [[False] * n for _ in range(n)]
    ans_blk, ans_cnt = 0, 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                visited, cnt = dfs(board, n, visited, [i, j], board[i][j], 1)
                ans_cnt = max(cnt, ans_cnt)
                if cnt >= 4:
                    ans_blk += 1
                    
    print(ans_blk, ans_cnt)
    

def main():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().split()))
    solution(board, n)
    
        
if __name__ == "__main__":
    main()