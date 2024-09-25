import sys

def merge_sort(arr, low, high):
	if low < high:
		mid = (low + high) // 2
		merge_sort(arr, low, mid)
		merge_sort(arr, mid + 1, high)
		arr = merge(arr, low, mid, high)
	return arr

def merge(arr, low, mid, high):
	arr_merged = []
	i, j = low, mid + 1
	
	while i <= mid and j <= high:
		if arr[i] <= arr[j]:
			arr_merged.append(arr[i])
			i += 1
		else:
			arr_merged.append(arr[j])
			j += 1
	# Adding remaining elements
	while i <= mid:
		arr_merged.append(arr[i])
		i += 1
	while j <= high:
		arr_merged.append(arr[j])
		j += 1
	
	for i in range(low, high + 1):
		arr[i] = arr_merged[i - low]
	
	return arr

def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	
	arr_sorted = merge_sort(arr, 0, n - 1)
	for num in arr_sorted:
		print(num, end = ' ')

if __name__ == "__main__":
	main()