import sys

def insertion_sort(arr, n):
    for i in range(n):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr_sorted = insertion_sort(arr, n)

    for num in arr_sorted:
        print(num, end = ' ')

if __name__ == "__main__":
    main()