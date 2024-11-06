directions = [[-1, 1], [-1, -1], [1, -1], [1, 1]]


def move(board, start, dist):
    cur = start
    res = 0
    for i in range(4):
        d = directions[i]
        for j in range(dist[i]):
            next = [cur[0] + d[0], cur[1] + d[1]]
            if board[next[0]][next[1]] == -1:
                return -1
            cur = next
            res += board[cur[0]][cur[1]]
    
    return res
            

def main():
    n = int(input())
    board = [[-1] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        board[i] = [-1] + list(map(int, input().split())) + [-1]
    
    answer = 0
    for i in range(2, n + 1):
        for j in range(n - i + 1, n):
            start = [i, j]
#           print(start, n - j, n - i)
            for ur in range(1, n - j + 1):
                res = 0
                for ul in range(1, n - ur):
                    dist = [ur, ul, ur, ul]
                    res = move(board, start, dist)
#                   print("dist", dist, "res", res)
                    answer = max(res, answer)
                if res == -1:
                    break
        
    print(answer)


if __name__ == "__main__":
    main()