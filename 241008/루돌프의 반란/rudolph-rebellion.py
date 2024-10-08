# N * N board, depicted as (r, c) starting with 1.

# Turn by Turn, M max

# Dist = (r1 - r2) ** 2 + (c1 - c2) ** 2

directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def get_dist(A, B):
    return (A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2

def move_valid(N, santas, k, pos):
    if not 0 <= pos[0] < N or not 0 <= pos[1] < N:
        return -1
    for i in range(len(santas)):
        if santas[i] != [-1, -1] and santas[i] == pos and k != i:
            return i

    return -2

def check_double(N, santas, res, k, dir, outs):
    while True:  # other santa
        if res == -2:
            return
        elif res == -1:
            outs[k] = 1
            santas[k] = [-1, -1]
            return
        else:
            k = res
            santas[k][0] += directions[dir][0]
            santas[k][1] += directions[dir][1]
            res = move_valid(N, santas, k, santas[k])

def move_collision(santas, dir, k, rudolf, C, D, stunned, turn, outs):
    if k == -1: # Rudolf
        for i in range(len(santas)):
            if santas[i] == rudolf:
                scores[i] += C
                santas[i][0] += C * directions[dir][0]
                santas[i][1] += C * directions[dir][1]
                stunned[i] = turn + 1 if stunned[i] < turn else stunned[i] + 1
                res = move_valid(N, santas, i, santas[i])
                check_double(N, santas, res, i, dir, outs)
    else: # Santa
        if santas[k] == rudolf:
            scores[k] += D
            dir = (dir + 4) % 8
            santas[k][0] += D * directions[dir][0]
            santas[k][1] += D * directions[dir][1]
            res = move_valid(N, santas, k, santas[k])
            stunned[k] = turn + 1 if stunned[k] < turn else stunned[k] + 1
            check_double(N, santas, res, k, dir, outs)


def check_avail(stunned, outs, i, turn):
    return stunned[i] >= turn or outs[i] != 0

def rudolf_move(santas, rudolf):
    cur_santa = 0
    cur_dist = 999
    dir = -1
    for i in range(len(santas)):
        dist = get_dist(santas[i], rudolf)
        if cur_dist > dist:
            cur_santa, cur_dist = i, dist
        elif cur_dist == dist:
            if santas[cur_santa][0] < santas[i][0]:
                cur_santa, cur_dist = i, dist
            elif santas[cur_santa][0] == santas[i][0]:
                if santas[cur_santa][1] < santas[i][1]:
                    cur_santa, cur_dist = i, dist

    best_pos = [0, 0]
    best_dist = cur_dist
    for i in range(8): # 8 directions
        n_row, n_col = rudolf[0] + directions[i][0], rudolf[1] + directions[i][1]
        if get_dist([n_row, n_col], santas[cur_santa]) < best_dist:
            best_pos = [n_row, n_col]
            best_dist = get_dist(best_pos, santas[cur_santa])
            dir = i

    rudolf[0], rudolf[1] = best_pos[0], best_pos[1]

    return dir


def santa_move(N, santas, k, rudolf):
    santa = santas[k]
    best_dist = get_dist(santa, rudolf)
    best_pos = [santa[0], santa[1]]
    dir = -1
    for i in range(0, 8, 2): # 8 directions
        new_pos = [santa[0] + directions[i][0], santa[1] + directions[i][1]]
        if move_valid(N, santas, k, new_pos) != -2:
            continue
        if get_dist(new_pos, rudolf) < best_dist:
            best_pos = new_pos
            best_dist = get_dist(new_pos, rudolf)
            dir = i

    santas[k] = best_pos
    return dir

N, M, P, C, D = map(int, input().split())
rudolf = list(map(int, input().split()))
rudolf[0], rudolf[1] = rudolf[0] - 1, rudolf[1] - 1
santas = [[0, 0] for _ in range(P)]
scores = [0] * P
stunned = [-1] * P
outs = [0] * P
for _ in range(P):
    pn, r, c = map(int, input().split())
    santas[pn - 1] = [r - 1, c - 1]

for turn in range(M):
    # print("------TURN", turn)
    # print("santas", santas)
    # print("rudolf", rudolf)
    # print("Stunned", stunned)
    dir = rudolf_move(santas, rudolf)
    # print("RudolfMove", rudolf)
    move_collision(santas, dir, -1, rudolf, C, D, stunned, turn, outs)
    for i in range(P):
        if not check_avail(stunned, outs, i, turn):
            dir = santa_move(N, santas, i, rudolf)
            if dir != -1: # Moved
                move_collision(santas, dir, i, rudolf, C, D, stunned, turn, outs)
    # print("SantaMove", santas)
    # print("Stunned", stunned)
    # print("Outs", outs)
    over = True
    for i in range(P):
        if outs[i] == 0:
            scores[i] += 1
            over = False
    if over:
        break
    # print("Score", scores)
print(*scores)