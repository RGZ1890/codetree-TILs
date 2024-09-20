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
    
    def FirstNode(self, Node):
        self.head = Node
        self.tail = Node
        self.prev = None
        self.next = None
        self.nodeCount = 1
        
    def clear(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0
        
    def size(self):
        return self.nodeCount
    
    def empty(self):
        return 1 if self.nodeCount == 0 else 0
    
    def front(self):
        return None if self.empty() else self.head.data
        
    def back(self):
        return None if self.empty() else self.tail.data
        
    def push_front(self, num):
        newNode = Node(num)
        newNode.next = self.head

        if (self.empty()):
            self.FirstNode(newNode)
        else:
            self.head.prev = newNode
            self.head = newNode
            newNode.prev = None
            self.nodeCount += 1
    
    def push_back(self, num):
        newNode = Node(num)
        newNode.prev = self.tail

        if (self.empty()):
            self.FirstNode(newNode)
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None
            self.nodeCount += 1
    
    def pop_front(self):
        if (self.empty()):
            print("List Empty.")
        elif (self.size() == 1):
            data = self.front()
            self.clear()
            return data
        else:
            temp = self.head
            temp.next.prev = None
            self.head = temp.next
            temp.next = None

            self.nodeCount -= 1
            return temp.data

    def pop_back(self):
        if (self.empty()):
            print("List Empty.")
        elif (self.size() == 1):
            data = self.front()
            self.clear()
            return data
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None

            self.nodeCount -= 1
            return temp.data

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