import sys

def radix_sort(arr_str, n): 
	digits = max(len(num) for num in arr_str)
	arr_str = [str(num).zfill(digits) for num in arr_str] # When there's elements with different digits
	
	for pos in range(digits - 1, -1, -1):
		ref_arr = [[] for _ in range(10)]
		for i in range(n):
			digit = int(arr_str[i][pos])
			ref_arr[digit].append(arr_str[i])
		
		result_arr = []
		for i in range(10):
			for j in range(len(ref_arr[i])):
				result_arr.append(ref_arr[i][j])
	
		arr_str = result_arr
	
	result_arr = list(map(int, result_arr))
	
	return result_arr

def main():
	n = int(sys.stdin.readline())
	arr = sys.stdin.readline().split()
	
	arr_sorted = radix_sort(arr, n)
	for num in arr_sorted:
		print(num, end = ' ')
	
if __name__ == "__main__":
	main()