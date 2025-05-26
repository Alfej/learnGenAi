class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.n = 0
    
    def enque(self,data):
        new_node = Node(data)
        if self.rear==None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.n += 1
        
    def deque(self):
        if self.front==None:
            raise Exception("Queue is empty")
        
        if self.front== self.rear:
            self.front = self.rear = None
        
        self.front = self.front.next
        self.n -= 1
        
    def traverse(self):
        if self.front==None:
            raise Exception("Queue is empty")
        
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

q = Queue()
q.enque(1)
q.enque(2)
q.enque(3)

q.traverse()  # Output: 1 2 3
q.deque()  # Removes 1\
q.traverse()  # Output: 2 3
q.enque(4)
q.traverse()  # Output: 2 3 4
q.deque()  # Removes 2
q.traverse()  # Output: 3 4

