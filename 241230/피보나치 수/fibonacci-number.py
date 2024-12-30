
memo = [-1] * 46
memo[1], memo[2] = 1, 1

def fib(N):
    if memo[N] != -1:
        return memo[N]
    memo[N] = fib(N - 1) + fib(N - 2)
    return memo[N]
    

def main():
    N = int(input())
    print(fib(N))


if __name__ == "__main__":
    main()