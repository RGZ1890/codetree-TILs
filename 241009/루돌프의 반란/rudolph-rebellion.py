moves = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

def get_dist(dept, dest):
    return (dept[0] - dest[0]) ** 2 + (dept[1] - dest[1]) ** 2

def move_valid(pos, santas, k, N):
    if not (1 <= pos[0] <= N and 1 <= pos[1] <= N):
        return -1
    if k != '-1': # Santa's move
        for i in range(1, P):
            if santas[i] != [-1, -1] and santas[i] == pos and i != k:
                return i
    return 0

def santa_move(santas, k, rudolf, N):
    cur_dist = get_dist(santas[k], rudolf)
    santa = santas[k]
    dir = -1
    for i in range(0, 8, 2):
        new_dest = [santas[k][0] + moves[i][0], santas[k][1] + moves[i][1]]
        new_dist = get_dist(new_dest, rudolf)
        if new_dist < cur_dist:
            if move_valid(new_dest, santas, k, N) == 0:
                santa = new_dest
                cur_dist = new_dist
                dir = i

    santas[k][0], santas[k][1] = santa[0], santa[1]

    return dir, cur_dist

def rudolf_move(rudolf, santas, P, N):
    closest = 0
    cur_dist = 5000
    cur_pos, dir = rudolf, 0
    for j in range(1, P):
        if santas[j] == [-1, -1]:
            continue
        dist = get_dist(rudolf, santas[j])
        if dist < cur_dist:
            cur_dist = dist
            closest = j
        elif dist == cur_dist:
            if santas[closest][0] < santas[j][0]:
                closest = j
            elif santas[closest][0] == santas[j][0] and santas[closest][1] < santas[j][1]:
                closest = j

    for i in range(8):
        new_dest = [rudolf[0] + moves[i][0], rudolf[1] + moves[i][1]]
        new_dist = get_dist(new_dest, santas[closest])
        if new_dist < cur_dist and move_valid(new_dest, santas, -1, N) != -1:
            cur_pos = new_dest
            cur_dist = new_dist
            dir = i

    rudolf[0], rudolf[1] = cur_pos[0], cur_pos[1]

    return dir, closest

def collateral(santas, k, dir, N, res):
    while res != 0:
        if res == -1:
            santas[k] = [-1, -1]
            res = 0
        else:
            k = res
            santas[k][0] += moves[dir][0]
            santas[k][1] += moves[dir][1]
            res = move_valid(santas[k], santas, k, N)

def hit_move(santas, k, dir, N, amt):
    santas[k][0] += amt * moves[dir][0]
    santas[k][1] += amt * moves[dir][1]
    res = move_valid(santas[k], santas, k, N)
    # -1: out, 0: valid, int: overlaps
    collateral(santas, k, dir, N, res)


N, M, P, C, D = map(int, input().split())
rr, rc = map(int, input().split())
rudolf = [rr, rc]
P += 1
santas = [[0, 0] for _ in range(P)]
stun = [0] * P
scores = [0] * P

for _ in range(P - 1):
    i, r, c = map(int, input().split())
    santas[i] = [r, c]

for turn in range(1, M + 1):
    # print("TURN", turn, santas[1:])

    dir, closest = rudolf_move(rudolf, santas, P, N)

    # print("RUDOLF", rudolf)
    if get_dist(rudolf, santas[closest]) == 0:
        # print("RUDOLF HIT")
        scores[closest] += C
        hit_move(santas, closest, dir, N, C)
        stun[closest] = turn + 1 if stun[closest] < turn else stun[closest] + 1

    for k in range(1, P):
        if santas[k] != [-1, -1] and stun[k] < turn:
            dir, dist = santa_move(santas, k, rudolf, N)
            if dist == 0:
                scores[k] += D
                hit_move(santas, k, (dir + 4) % 8, N, D)
                stun[k] = turn + 1 if stun[k] < turn else stun[k] + 1
    #             print("SANTA HIT", santas[k])
    #
    # print("SANTA", santas[1:])
    # print("STUN", stun[1:])
    is_over = True
    for k in range(1, P):
        if santas[k] != [-1, -1]:
            is_over = False
            scores[k] += 1
    # print("SCORES", scores[1:], is_over)
    if is_over:
        break

print(*scores[1:])