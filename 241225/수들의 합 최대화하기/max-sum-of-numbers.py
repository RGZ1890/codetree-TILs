
def solution(board, n, row, visited, cur, ans):
#   print("ROW", row, "VISITED", visited, "CUR", cur, "ANS", ans)
    if row == n:
        return max(ans, cur)
    
    for col in range(n):
        if visited[col] == False:
            visited[col] = True
            ans = solution(board, n, row + 1, visited, cur + board[row][col], ans)
            visited[col] = False
    
    return ans
    


def main():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, input().split()))
    
    visited = [False] * (n + 1)
    ans = solution(board, n, 0, visited, 0, 0)
    print(ans)
    
    
if __name__ == "__main__":
    main()
    