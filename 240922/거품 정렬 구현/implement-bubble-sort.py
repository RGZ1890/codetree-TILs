import sys

def BubbleSort(arr, n):
    sorted = False
    while (not sorted):
        sorted = True
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_sorted = BubbleSort(arr, n)

    for i in range(n):
        print(arr_sorted[i], end = ' ')



if __name__ == "__main__":
    main()