def calc_move(pos, dir):
    new_pos = [p for p in pos]
    for l in range(2):
        new_pos[l] += dir[l]
        new_pos[l + 2] += dir[l]
    return new_pos


def find_collide(knights_pos, next_pos, colliding, dir):
    coords = []
    for i in range(next_pos[0], next_pos[2]):
        for j in range(next_pos[1], next_pos[3]):
            coords.append([i, j])
    for k in range(1, N + 1):
        if k not in colliding:
            pos = knights_pos[k]
            for c in coords:
                if pos[0] <= c[0] < pos[2] and pos[1] <= c[1] < pos[3]:
                    colliding.append(k)
                    colliding = find_collide(knights_pos, calc_move(pos, dir), colliding, dir)
                    break

    return colliding

def wall_touch(knights_pos, colliding, dir):
    new_pos = [k for k in knights_pos]
    for c in colliding:
        new_pos[c] = calc_move(new_pos[c], dir)
        # print("WALLTOUCH", c, new_pos[c])
        for j in range(new_pos[c][0], new_pos[c][2]):
            for k in range(new_pos[c][1], new_pos[c][3]):
                if board[j][k] == 2:
                    return True

    # print("UPDATE", new_pos)
    for c in colliding:
        knights_pos[c] = new_pos[c]
    return False

def update_hp(i, colliding, board, knights_pos, hp_after):
    for c in colliding:
        if i != c:
            for j in range(knights_pos[c][0], knights_pos[c][2]):
                for k in range(knights_pos[c][1], knights_pos[c][3]):
                    if board[j][k] == 1:
                        hp_after[c] -= 1
            if hp_after[c] < 0:
                knights_pos[c] = [-5] * 4


directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = 0
L, N, Q = map(int, input().split())

board = [[2] * (L + 2) for _ in range(L + 2)]
for i in range(1, L + 1):
    board[i] = [2] + list(map(int, input().split())) + [2]

k_board = [row[:] for row in board]
for i in range(L + 2):
    for j in range(L + 2):
        if board[i][j] == 2:
            k_board[i][j] = -1

hp_before = [0] * (N + 1)
hp_after = [0] * (N + 1)
knights_pos = [[0, 0, 0, 0] for _ in range(N + 1)]

for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    hp_before[i] = k
    hp_after[i] = k
    knights_pos[i] = [r, c, r + h, c + w]

    for j in range(r, r + h):
        for k in range(c, c + w):
            k_board[j][k] = i

for _ in range(Q):
    # print("___________________________________________")
    i, d = map(int, input().split())
    if hp_after[i] != 0:
        dir = directions[d]
        next_pos = calc_move(knights_pos[i], dir)
        # print("i, d", [i, d], next_pos, knights_pos[1:])
        colliding = find_collide(knights_pos, next_pos, [i], dir)
        # print("Colliding", colliding)
        if wall_touch(knights_pos, colliding, dir):
            continue
        # print("knights_pos", knights_pos[1:])
        update_hp(i, colliding, board, knights_pos, hp_after)
    # for row in k_board:
    #     print(row)

for i in range(N + 1):
    if hp_after[i] != 0:
        ans += hp_before[i] - hp_after[i]
print(ans)

#
# print("BOARD")
# for row in board:
#     print(row)
#
# print("K_BOARD")
# for row in k_board:
#     print(row)