dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(board, visited, cur, cnt):
    for d in dirs:
        new_pos = [cur[0] + d[0], cur[1] + d[1]]
        if board[new_pos[0]][new_pos[1]] != 0 and \
        not visited[new_pos[0]][new_pos[1]]:
            visited[new_pos[0]][new_pos[1]] = True
            visited, cnt = dfs(board, visited, new_pos, cnt + 1)
    
    return visited, cnt


def solution(board, n):
    ans = []
    visited = [[False] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] != 0 and not visited[i][j]:
                visited[i][j] = True
                visited, cnt = dfs(board, visited, [i, j], 1)
                ans.append(cnt)
                
    return sorted(ans)


def main():
    n = int(input())
    board = [[0] * (n + 2) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        tmp = list(map(int, input().split()))
        board[i] = [0] + tmp + [0]
    
    ans = solution(board, n)
    print(len(ans), *ans, sep = '\n')
        

if __name__ == "__main__":
    main()