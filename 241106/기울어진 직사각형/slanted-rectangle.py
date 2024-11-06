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


def getRes(board, n, start):
    res = 0
    r, c = start[0], start[1]
    for ur in range(1, min(n + 1 - c, r)):
        for ul in range(1, min(c, r)):
            dist = [ur, ul, ur, ul]
            res = max(move(board, start, dist), res)
#           print("dist", dist, "res", res)
        if res == -1:
            break

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
#           print(start)
            answer = max(getRes(board, n, start), answer)
            
    print(answer)


if __name__ == "__main__":
    main()