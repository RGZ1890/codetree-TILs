def get_score(m, moves, n, k, choices):
    pos = [1 for _ in range(k)]
    for i in range(n):
        pos[choices[i]] += moves[i]

    score = sum(1 for p in pos if p >= m)
#   print("moves", moves, "pos", pos, "choices", choices, "score", score)
    return score


def solution(m, k, moves, n, choices, i, score):
    if i == n:
        return get_score(m, moves, n, k, choices)
    for j in range(k):
        score = max(score, solution(m, k, moves, n, choices + [j], i + 1, score))
        
    return score


def main():
    n, m, k = map(int, input().split())
    moves = list(map(int, input().split()))
    score = solution(m, k, moves, n, [], 0, 0)
    print(score)


if __name__ == "__main__":
    main()