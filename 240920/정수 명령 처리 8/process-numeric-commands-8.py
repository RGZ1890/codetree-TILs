class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DLList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0
    
    def push_front(self, num):
        newNode = Node(num)
        newNode.next = self.head

        if (self.head != None):
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None
        
        else:
            self.head = newNode
            self.tail = newNode
            newNode.prev = None

        self.nodeCount += 1
    
    def push_back(self, num):
        newNode = Node(num)
        newNode.prev = self.tail

        if (self.tail != None):
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None
        
        else:
            self.head = newNode
            self.tail = newNode
            newNode.next = None
        
        self.nodeCount += 1
    
    def pop_front(self):
        if (self.head == None):
            print("List Empty.")
        
        elif (self.head.next == None):
            temp = self.head

            self.head = None
            self.tail = None
            self.nodeCount = 0
            return temp.data
        
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.nodeCount -= 1
            return temp.data

    def pop_back(self):
        if (self.tail == None):
            print("List Empty.")
        
        elif (self.tail.prev == None):
            temp = self.tail

            self.head = None
            self.tail = None
            self.nodeCount = 0
            return temp.data
        
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.nodeCount -= 1
            return temp.data
        
    def size(self):
        return self.nodeCount
    
    def empty(self):
        return 1 if self.nodeCount == 0 else 0
    
    def front(self):
        if (self.head == None):
            print("List Empty.")
        else:
            return self.head.data

    def back(self):
        if (self.tail == None):
            print("List Empty.")
        else:
            return self.tail.data

import sys

def main():
    N = int(sys.stdin.readline())
    dll = DLList()
    for i in range(N):
        cmd = sys.stdin.readline().split()
        if (cmd[0] == "push_back"):
            dll.push_back(int(cmd[1]))
        elif (cmd[0] == "push_front"):
            dll.push_front(int(cmd[1]))
        elif (cmd[0] == "pop_back"):
            print(dll.pop_back())
        elif (cmd[0] == "pop_front"):
            print(dll.pop_front())
        elif (cmd[0] == "size"):
            print(dll.size())
        elif (cmd[0] == "empty"):
            print(dll.empty())
        elif (cmd[0] == "front"):
            print(dll.front())
        elif (cmd[0] == "back"):
            print(dll.back())
        else:
            print("Error.")

if (__name__ == "__main__"):
    main()