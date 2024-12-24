INF = 2 ** 30

def getVal(nums, refs, opers, N):
    res = refs[nums[0]]
    for i in range(N):
        n = refs[nums[i + 1]]
        if opers[i] == '+':
            res += n
        elif opers[i] == '-':
            res -= n
        elif opers[i] == '*':
            res *= n
            
#   print("nums", nums, "refs", refs, "res", res)
    return res


def solution(nums, refs, i, opers, N, val):
    if i == 6:
        return getVal(nums, refs, opers, N)
    for n in range(1, 5):
        refs[i] = n
        val = max(val, solution(nums, refs, i + 1, opers, N, val))
    
    return val


def main():
    s = input()
    N = 0
    nums, opers = [], []
    refs = [1, 1, 1, 1, 1, 1]
    for c in s:
        if c.isalpha():
            n = ord(c) - ord('a')
            nums.append(n)
        else:
            N += 1
            opers.append(c)
    
    ans = solution(nums, refs, 0, opers, N, -INF)
    print(ans)


if __name__ == "__main__":
    main()