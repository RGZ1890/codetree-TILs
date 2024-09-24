import sys

def radix_sort(arr_str, n):
    # Determine the maximum number of digits
    digits = max(len(num) for num in arr_str)

    # Initialize an array to store sorted results
    result_arr = [None] * n

    # Perform counting sort for each digit position
    for pos in range(digits - 1, -1, -1):
        # Create buckets for each digit
        ref_arr = [[] for _ in range(10)]

        for i in range(n):
            # Right justify the number by filling with zeros
            digit = int(arr_str[i].zfill(digits)[pos])
            ref_arr[digit].append(arr_str[i])

        # Flatten the buckets back into the result array
        idx = 0
        for i in range(10):
            for value in ref_arr[i]:
                result_arr[idx] = value
                idx += 1

        # Update arr_str to the newly sorted result
        arr_str = result_arr.copy()

    # Convert the sorted strings back to integers
    result_arr = list(map(int, arr_str))

    return result_arr

def main():
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().split()

    arr_sorted = radix_sort(arr, n)
    for num in arr_sorted:
        print(num, end=' ')

if __name__ == "__main__":
    main()