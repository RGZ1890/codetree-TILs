INF = 10001

def solution(board, n, visited, row, cur, ans):
    if row == n:
        return max(cur, ans)
    
    for col in range(n):
        if not visited[col]:
            visited[col] = True
            ans = solution(board, n, visited, row + 1, min(cur, board[row][col]), ans)
            visited[col] = False
    
    return ans


def main():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    visited = [0] * n
    for i in range(n):
        board[i] = list(map(int, input().split()))

    print(solution(board, n, visited, 0, INF, 0))

if __name__ == "__main__":
    main()