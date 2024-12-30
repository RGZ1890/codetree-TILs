
stairs = [-1] * 1001
stairs[1], stairs[2], stairs[3] = 0, 1, 1


def DP(N):
    if stairs[N] != -1:
        return stairs[N]
    stairs[N] = DP(N - 2) + DP(N - 3)
    return stairs[N]
    
    
def main():
    n = int(input())
    print(DP(n) % 10007)
    

if __name__ == "__main__":
    main()