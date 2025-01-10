import sys

NOPE = 0

def solution(grid, n):
    ans = NOPE
    board = [[NOPE] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        board[i] = [NOPE] + grid[i - 1] + [NOPE]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            board[i][j] += max(board[i - 1][j], board[i][j - 1])
    
    return max(board[n])


def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(solution(grid, n))
        

if __name__ == "__main__":
    main()
    