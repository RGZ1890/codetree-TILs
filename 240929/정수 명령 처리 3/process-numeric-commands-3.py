import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    deq = deque()

    for i in range(N):
        args = sys.stdin.readline().split()
        comm = args[0]
        if comm == "push_front":
            deq.appendleft(int(args[1]))
        elif comm == "push_back":
            deq.append(int(args[1]))
        elif comm == "pop_front":
            print(deq.popleft())
        elif comm == "pop_back":
            print(deq.pop())
        elif comm == "size":
            print(len(deq))
        elif comm == "empty":
            print(0 if deq else 1)
        elif comm == "front":
            print(deq[0])
        elif comm == "back":
            print(deq[-1])
        else:
            raise Exception("Wrong command.")

if __name__ == "__main__":
    main()