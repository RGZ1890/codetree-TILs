import sys

def selection_sort(arr, n):
    for i in range(n):
        minidx = i
        for j in range(i + 1, n):
            minidx = j if arr[j] < arr[minidx] else minidx
        if minidx != i:
            arr[i], arr[minidx] = arr[minidx], arr[i]

    return arr


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    arr_sorted = selection_sort(arr, n)
    for i in range(n):
        print(arr[i], end = ' ')

if __name__ == "__main__":
    main()