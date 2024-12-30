MOD = 1000000007
block = [-1] * 1001
block[0], block[1], block[2], block[3] = 0, 2, 7, 22

def DP(N):
    if block[N] != -1:
        return block[N]
    block[N] = (DP(N - 1) + DP(N - 2)) % MOD
    return block[N]


def main():
    n = int(input())
    print(DP(n))
    
    
if __name__ == "__main__":
    main()