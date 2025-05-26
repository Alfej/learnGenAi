class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    def __len__(self):
        return self.n
    
    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.n += 1
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.n += 1
    
    def __str__(self):
        curr = self.head
        res = ''
        while curr:
            res = res+ str(curr.data) + '->' 
            curr = curr.next
        
        return res[:-2]  # Remove the last '->'
        
        
a = Node(1)
b = Node(2)
a.next = b
c = Node(3)
b.next = c
print(a.data)
print(id(a)) # Output: 1
print(a.next)
print(b.data)
print(id(b)) # Output: None
print(b.next)
print(c.data)
print(id(c)) # Output: None
print(c.next)

l = LinkedList()
l.append(5)
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.append(4)

print(l) # Output: 3 2 1
print(len(l)) # Output: 5

