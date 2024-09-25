import sys

def select_pivot(arr, low, high):
	mid = (low + high) // 2
	tgt = high
	if high - low > 3:
		if (arr[low] <= arr[mid] <= arr[low]) or (arr[high] <= arr[mid] <= arr[low]):
			tgt = mid
		elif (arr[mid] <= arr[low] <= arr[high]) or (arr[high] <= arr[low] <= arr[mid]):
			tgt = low
		arr[tgt], arr[high] = arr[high], arr[tgt]
	return arr[high]
		
def partition(arr, low, high):
	pivot = select_pivot(arr, low, high)
	i = low - 1
	
	for j in range(low, high):
		if arr[j] < pivot:
			i += 1
			arr[i], arr[j] = arr[j], arr[i]
	
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	
	return i + 1

def quick_sort(arr, low, high):
	if low < high:
		pos = partition(arr, low, high)
		
		quick_sort(arr, low, pos - 1)
		quick_sort(arr, pos + 1, high)

def main():
	n = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	
	quick_sort(arr, 0, n - 1)
	for num in arr:
		print(num, end = ' ')

if __name__ == "__main__":
	main()