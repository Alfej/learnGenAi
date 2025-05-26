# stack using linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    
    def isempty(self):
        return self.top == None

    def push(self,data):
        new_node = Node(data)
        if self.isempty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.n += 1
    
    def pop(self):
        if self.isempty():
            raise Exception("Stack is empty")
        popped_node = self.top
        self.top = self.top.next
        self.n -= 1
        return popped_node.data
    
    def traversre(self):
        curr = self.top
        while curr:
            print(curr.data, end=' ')
            curr = curr.next
    
    def peak(self):
        if self.isempty():
            raise Exception("Stack is empty")
        return self.top.data
        
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Top element:", stack.peak())  # Output: Top element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Top element after pop:", stack.peak())  # Output: Top element after pop: 2
stack.push(4)
print("Top element after pushing 4:", stack.peak())  # Output: Top element after pushing 4: 4
print("Stack elements:")
stack.traversre()  # Output: Stack elements: 4 2 1

# Implementing a stack using a list
class StackList:
    def __init__(self,size):
        self.size = size
        self.stack = [None]*size
        self.top = -1
        
    def push(self,data):
        if self.top == self.size - 1:
            raise Exception("Stack overflow")
        self.top += 1
        self.stack[self.top] = data
    
    def pop(self):
        if self.top == -1:
            raise Exception("Stack underflow")
        popped_data = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return popped_data
    
    def peak(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        return self.stack[self.top]
    
    def isempty(self):
        return self.top == -1
    
    def traverse(self):
        for i in range(self.top, -1, -1):
            print(self.stack[i], end=' ')
    
stack = StackList(4)
stack.push(1)
stack.push(2)
stack.push(3)
print("Top element:", stack.peak())  # Output: Top element: 3
print("Popped element:", stack.pop())  # Output: Popped element: 3
print("Top element after pop:", stack.peak())  # Output: Top element after pop: 2
stack.push(4)
print("Top element after pushing 4:", stack.peak())  # Output: Top element after pushing 4: 4
print("Stack elements:")
stack.traverse()  # Output: Stack elements: 4 2 1
    
    