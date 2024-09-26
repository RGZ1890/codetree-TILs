import sys

def heapify(arr_heap, n, idx):
	lc, rc = idx * 2, idx * 2 + 1
	largest = idx
	
	if n >= lc and arr_heap[largest] < arr_heap[lc]:
		largest = lc
	if n >= rc and arr_heap[largest] < arr_heap[rc]:
		largest = rc

	if largest != idx:
		arr_heap[largest], arr_heap[idx] = arr_heap[idx], arr_heap[largest]
		heapify(arr_heap, n, largest)
		
def heap_sort(arr, n):
	arr_heap = arr
	for i in range(n // 2, 0, -1):
		heapify(arr_heap, n, i)
	for i in range(n, 1, -1):
		arr_heap[1], arr_heap[i] = arr_heap[i], arr_heap[1]
		heapify(arr_heap, i - 1, 1)
	
	return arr_heap[1:]

def main():
	n = int(sys.stdin.readline())
	arr = [0] + list(map(int, sys.stdin.readline().split()))
	
	arr_sorted = heap_sort(arr, n)
	
	print(*arr_sorted)

if __name__ == "__main__":
	main()