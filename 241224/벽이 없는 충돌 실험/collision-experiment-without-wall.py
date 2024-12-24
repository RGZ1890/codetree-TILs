ddict = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}

def collision(position_map):
    eliminated = set()

    for pos, marbles_at_pos in position_map.items():
        if len(marbles_at_pos) > 1:
            survivor = marbles_at_pos[0]
            for m in marbles_at_pos[1:]:
                if m[2] > survivor[2] \
                or (m[2] == survivor[2] and m[5] > survivor[5]):
                    survivor = m
            for m in marbles_at_pos:
                if m != survivor:
                    eliminated.add(m[5])
                    
    return eliminated


def solution(marbles):
    t, ct = 0, -1
    while t < 4000 and marbles:
        t += 1
        position_map = {}

        for m in marbles:
            m[0] += m[3]
            m[1] += m[4]
            pos = (m[0], m[1])
            if pos in position_map:
                position_map[pos].append(m)
            else:
                position_map[pos] = [m]

        eliminated = collision(position_map)
        if eliminated:
            ct = t
            marbles = [m for m in marbles if m[5] not in eliminated]

    return ct

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        marbles = []
        for i in range(N):
            s = input().split()
            x, y, w = map(int, s[:3])
            d = ddict[s[3]]
            marbles.append([x * 2, y * 2, w, d[0], d[1], i])  # Include index for tie-breaking

        ct = solution(marbles)
        print(ct)

if __name__ == "__main__":
    main()
