import sys

max_size = 100

class Stack:
	
	def __init__(self):
		self.items = [0] * max_size
		self.size = 0
	
	def empty(self):
		return 0 if self.size else 1
	
	def top(self):
		if self.empty():
			raise Exception("Stack is Empty")
		return self.items[self.size - 1]
	
	def push(self, num):
		self.size += 1
		self.items[self.size - 1] = num
		
	def pop(self):
		if self.empty():
			raise Exception("Stack is empty")
		self.size -= 1
		return self.items[self.size]
	
def main():
	stack = Stack()

	N = int(sys.stdin.readline())
	for i in range(N):
		args = sys.stdin.readline().split()
		cmd = args[0]
		if cmd == "push":
			stack.push(int(args[1]))
		elif cmd == "pop":
			print(stack.pop())
		elif cmd == "size":
			print(stack.size)
		elif cmd == "empty":
			print(stack.empty())
		elif cmd == "top":
			print(stack.top())
		else:
			raise Exception("Wrong argument.")


if __name__ == "__main__":
	main()