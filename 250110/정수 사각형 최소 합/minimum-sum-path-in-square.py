NOPE = 1000001


def solution(board, N):
    cboard = [[NOPE] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        cboard[i] = [NOPE] + board[i - 1] + [NOPE]
    
    for i in range(1, N + 1):
        for j in range(N, 0, -1):
            if i == 1 and j == N:
                continue
            cboard[i][j] += min(cboard[i - 1][j], cboard[i][j + 1])
            
    return cboard[N][1]


def main():
    N = int(input())
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))
    
    print(solution(board, N))
    

if __name__ == "__main__":
    main()