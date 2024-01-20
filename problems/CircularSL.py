class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Circular:
    def __init__(self):
        self.head = None

    def add_ele(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            new_node.next = self.head  
        else:
            current = self.head
            while current.next != self.head:
                current=current.next
            current.next = new_node
            new_node.next = self.head

    def traverse(self):
        if self.head == None:
            print("list is empty")
        else:    
            current = self.head
            while True:
                print(current.data, end=" ")
                current = current.next
                if current == self.head:
                    break


cll1 = Circular()
cll1.add_ele(4)
cll1.add_ele(5) 
cll1.add_ele(7) 
cll1.add_ele(9)

print("\nOriginal circular linked list:")
            
        
cll1.traverse()
