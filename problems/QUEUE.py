queue= []
def enqueue():
    element = int(input("Enter element to add: "))
    queue.append(element)
    print(queue)

def dequeue():
    if not queue:
        print("queue is empty")
    else:
        n = int(input("position: "))
        if n in range(len(queue)):
            pop = queue.pop(n)
            print(f"popped element:{pop}")
            print(queue)
        else:
            print("position is out of range")    

def display():
    print(queue)

while True:
    choice = int(input("1 = push, 2 = pop, 3 = exit: "))
    if choice == 1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("invalid")              
