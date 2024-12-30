
block = [-1] * 1001
block[0], block[1], block[2] = 0, 1, 2

def DP(N):
    if block[N] != -1:
        return block[N]
    block[N] = (DP(N - 1) + DP(N - 2)) % 10007
    return block[N]


def main():
    n = int(input())
    print(DP(n))
    

if __name__ == "__main__":
    main()