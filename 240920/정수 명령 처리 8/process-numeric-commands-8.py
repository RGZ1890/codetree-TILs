class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.node_count = 0
        
    def is_empty(self):
        return self.node_count == 0
    
    def size(self):
        return self.node_count
    
    def front(self):
        return self.head.data if self.head else None
    
    def back(self):
        return self.tail.data if self.tail else None
    
    def push_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.node_count += 1
        
    def push_back(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.node_count += 1
        
    def pop_front(self):
        if self.is_empty():
            raise IndexError("List is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.node_count -= 1
        return data
    
    def pop_back(self):
        if self.is_empty():
            raise IndexError("List is empty")
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        self.node_count -= 1
        return data
    
    def clear(self):
        self.head = self.tail = None
        self.node_count = 0

import sys

def main():
    N = int(sys.stdin.readline())
    dll = DoublyLinkedList()
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
            print(1 if dll.is_empty() else 0)
        elif (cmd[0] == "front"):
            print(dll.front())
        elif (cmd[0] == "back"):
            print(dll.back())
        else:
            print("Error.")

if (__name__ == "__main__"):
    main()