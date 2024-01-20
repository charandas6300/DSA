class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_ele(self,new_node):
        if self.head == None:
            self.head = Node(new_node)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(new_node)    

    def add_at_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        current = self.head
        while current.next == None:
            current = current.next
        current.next = new_node               

    def add_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = slef.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while current != None and count < position:
                prev = current
                current = current.next
                count += 1
            if current == None:
                print("Position out of range")
                return
            prev.next = new_node
            new_node.next = current    

    def delete_element(self, data):
        if self.head == None:
            print("list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current != None and current.data != data:
            prev = current
            current = current.next

        if current == None:
            print("data not found")
            return
        t =current 
        print(f"deleted ele:{t.data}")   
        prev.next = current.next 
        del current               

    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            current = self.head
            while current != None:
                print(current.data)
                current=current.next


# Creating a linked list instance
LL = LinkedList()

# Adding elements to the list
LL.add_ele(10)
LL.add_ele(20)
LL.add_ele(30)
LL.add_ele(40)
LL.add_ele(50)

# Traversing the list
print("Linked List:")
LL.print_LL()

LL.add_at_end(34)
LL.print_LL()
# Adding an element at a given position
# LL.add_at_position(15, 1)

# print("Linked List after adding at position:")
# LL.print_LL()

# # Deleting an element
# LL.delete_element(30)

# print("Linked List after deletion:")
# LL.print_LL()