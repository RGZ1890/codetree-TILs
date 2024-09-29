import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    dq = deque()
    for i in range(N):
        dq.append(i + 1)
    
    for _ in range(N - 1):
        dq.popleft()
        dq.append(dq.popleft())
    
    print(dq[0])

if __name__ == "__main__":
    main()