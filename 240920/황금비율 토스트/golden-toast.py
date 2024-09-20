# Node 클래스를 만들어줍니다.
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
        self.prev = None


# 이중 연결 리스트 클래스를 만들어줍니다.
class DoublyLinkedList:
    def __init__(self):
        self.END = Node(-1)                
        self.head = self.END
        self.tail = self.END
  
    def push_front(self, new_data):        
        new_node = Node(new_data)          
        new_node.next = self.head          

        self.head.prev = new_node          
        self.head = new_node
        new_node.prev = None

    def push_back(self, new_data):        
        if self.begin() == self.end():    
            self.push_front(new_data)     
            
        else:
            new_node = Node(new_data)     
            new_node.prev = self.tail.prev
            self.tail.prev.next = new_node
            new_node.next = self.tail     
            self.tail.prev = new_node     

    def erase(self, node):
        next_node = node.next

        if node == self.begin():           
            temp = self.head          
            temp.next.prev = None          
            self.head = temp.next          
            temp.next = None               

        else:                              
            node.prev.next = node.next     
            node.next.prev = node.prev     
            node.prev = None               
            node.next = None               

        return next_node
    
    def insert(self, node, new_data):
        if node == self.end():       
            self.push_back(new_data) 

        elif node == self.begin():   
            self.push_front(new_data)

        else:                        
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node     
            node.prev.next = new_node
            node.prev = new_node     

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail

import sys

def main():
    l = DoublyLinkedList()
    n, m = map(int, sys.stdin.readline().split())
    bread = sys.stdin.readline().strip()
    for b in bread:
        l.push_back(b)
    
    it = l.end()
    
    for i in range(m):
        args = sys.stdin.readline().split()
        com = args[0]
#       print(com, end = ' ')
        if (com == 'L'):
            if (it != l.begin()):
                it = it.prev
        elif (com == 'R'):
            if (it != l.end()):
                it = it.next
        elif (com == 'D'):
            if (it != l.end()):
                l.erase(it)
        elif (com == 'P'):
            l.insert(it, args[1])
#       print("it:", it.data)

    it = l.begin()
    while (it != l.end()):
        print(it.data, end = '')
        it = it.next

if (__name__ == "__main__"):
    main()