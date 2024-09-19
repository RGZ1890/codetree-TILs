import sys

def push_back(dynArray, num):
    num = int(num)
    dynArray.append(num)
    return dynArray

def pop_back(dynArray):
    dynArray.pop()
    return dynArray

def size_arr(dynArray):
    print(len(dynArray))

def get_arr(dynArray, idx):
    idx = int(idx) - 1
    print(dynArray[idx])

def main():
    N = int(sys.stdin.readline())
    dynArray = []
    for i in range(N):
        comm = sys.stdin.readline().split()
        if comm[0] == "push_back":
            dynArray = push_back(dynArray, comm[1])
        elif comm[0] == "pop_back":
            dynArray = pop_back(dynArray)
        elif comm[0] == "size":
            size_arr(dynArray)
        elif comm[0] == "get":
            get_arr(dynArray, comm[1])
        else:
            pass

if (__name__ == "__main__"):
    main()