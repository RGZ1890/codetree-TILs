dirs = [[1, 0], [0, 1]]

def solution(board, end, cur, visited, res):
    if cur == end:
        return 1
    
    for d in dirs:
        new_pos = [cur[0] + d[0], cur[1] + d[1]]
        if board[new_pos[0]][new_pos[1]] == 1 and \
        not visited[new_pos[0]][new_pos[1]]:
            visited[new_pos[0]][new_pos[1]] = True
            if solution(board, end, new_pos, visited, res):
                return 1
            
    return 0


def main():
    n, m = map(int, input().split())
    board = [[0] * (m + 2) for _ in range(n + 2)]
    visited = [[False] * (m + 2) for _ in range(n + 2)]
    visited[1][1] = True
    for i in range(1, n + 1):
        inp = list(map(int, input().split()))
        board[i] = [0] + inp + [0]
        
    print(solution(board, [n, m], [1, 1], visited, 0))
        
        
if __name__ == "__main__":
    main()