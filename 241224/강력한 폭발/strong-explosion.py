def blowBomb(tmpBoard, n, nr, nc, score):
    if 0 <= nr < n and 0 <= nc < n \
    and tmpBoard[nr][nc] == 0:
        tmpBoard[nr][nc] = -1
        score += 1
        
    return tmpBoard, score

def cntScore(board, n, bombs):
    tmpBoard = [row[:] for row in board]
    score = 0
    for b in bombs:
        if tmpBoard[b[0]][b[1]] == 1:
            for r in range(-2, 3):
                tmpBoard, score = blowBomb(tmpBoard, n, b[0] + r, b[1], score)
        elif tmpBoard[b[0]][b[1]] == 2:
            for r, c in ([-1, 0], [0, 1], [1, 0], [0, -1]):
                tmpBoard, score = blowBomb(tmpBoard, n, b[0] + r, b[1] + c, score)
        elif tmpBoard[b[0]][b[1]] == 3:
            for r, c in ([-1, -1], [-1, 1], [1, 1], [1, -1]):
                tmpBoard, score = blowBomb(tmpBoard, n, b[0] + r, b[1] + c, score)
        else:
            continue
        score += 1
    
    return score


def solution(board, n, bombs, m, b, score):
    if b == m:
        return cntScore(board, n, bombs)
    
    for i in range(1, 4):
        board[bombs[b][0]][bombs[b][1]] = i
        score = max(score, solution(board, n, bombs, m, b + 1, score))
    
    return score


def main():
    n = int(input())
    board = [[0] * n for _ in range(n)]
    bombs = []
    for i in range(n):
        board[i] = list(map(int, input().split()))
        for j in range(n):
            if board[i][j] == 1:
                bombs.append([i, j])
    
    answer = solution(board, n, bombs, len(bombs), 0, 0)
    
    print(answer)

if __name__ == "__main__":
    main()