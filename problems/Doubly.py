class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoblyLL:
    def __init__(self):
        self.head = None

    def add_ele(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node
            new_node.prev = current   

    def add_ele_at_position(self, data, position):
        if position < 0:
            print("invalid position")
            return
        new_node = Node(data)  
        if position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            index = 0
            while current.next and index < position - 1:
                current = current.next
                index += 1
            if index == position - 1:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev =new_node
                current.next = new_node
            else:
                print('Invalid Position')
                
    

    def delete_element(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        print("element not found")    

    def traverse(self):
        if self.head == None:
            print("list is empthy")
        else:    
            current = self.head
            while current!=None:
                print(current.data,end="->")
                current=current.next
            print("Null")    

        

DLL1 = DoblyLL()
DLL1.add_ele(3)
DLL1.add_ele(4)
DLL1.add_ele(5)
DLL1.add_ele(6)

DLL1.traverse()
data = int(input("data:"))
pos = int(input("position:"))

DLL1.add_ele_at_position(data,pos)


dle = int(input("delete:"))
DLL1.delete_element(dle)

DLL1.traverse()