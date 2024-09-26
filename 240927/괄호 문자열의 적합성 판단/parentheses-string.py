# Brief data structure using Python List

import sys

def parenthese(par, stack):
    for letter in par:
        if letter == '(':
            stack.append(letter)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

    return not len(stack)

def main():
    par = sys.stdin.readline().rstrip()
    stack = []
    res = parenthese(par, stack)
    print("Yes" if res else "No")
    

if __name__ == "__main__":
    main()