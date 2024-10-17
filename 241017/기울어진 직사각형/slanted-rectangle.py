import sys


dirs = [[-1, 1], [-1, -1], [1, -1], [1, 1]]

def get_area(board, n, start):
    score = 0
    cur = [start[0], start[1]]
    
    for d in range(4):
        while True:
            if d == 3 and cur == start:
                return score
#           print("CUR", cur, d, end = ' ')
            score += board[cur[0]][cur[1]]
            next = [cur[0] + dirs[d][0], cur[1] + dirs[d][1]]
#           print("NEXT", next, start)
            if d == 3:
                if 0 <= next[0] < n and 0 <= next[1] < n:
                    cur = next
            else:
                turn = [next[0] + dirs[d + 1][0], next[1] + dirs[d + 1][1]]
                if 0 <= next[0] < n and 0 <= next[1] < n and \
                    0 <= turn[0] < n and 0 <= turn[1] < n:
                        cur = next
                else:
                    cur = [cur[0] + dirs[d + 1][0], cur[1] + dirs[d + 1][1]]
                    break


def main():
    n = int(sys.stdin.readline())
    board = [[0] * n for _ in range(n)]

    for i in range(n):
        board[i] = list(map(int, sys.stdin.readline().split()))
    
    ans = 0
    for i in range(1, n // 2 + 1):
        res = get_area(board, n, [n - 1, i])
        ans = max(ans, res)
    
    print(ans)


if __name__ == "__main__":
    main()