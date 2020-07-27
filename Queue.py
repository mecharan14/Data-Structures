import os
class Queue:
    def __init__(self, max_size):
        self.max = max_size
        self.q = []
        self.front = -1
        self.rear = -1
    def isEmpty(self):
        return (self.front == -1 or self.front > self.rear)
    def isFull(self):
        return self.rear == self.max-1
    def peek(self):
        if self.isEmpty():
            print("** Queue is empty to peek. **")
            return
        print("The first element is: " + str(self.q[self.front]))
    def enqueue(self, data):
        if not self.isFull():
            if self.isEmpty():
                self.front = 0
                self.rear = 0
            else:
                self.rear += 1
            self.q.insert(self.rear, data)
            print("** " + str(data) + " added to queue. **")
        else:
            print("** Queue is full. **")
    def dequeue(self):
        if  not self.isEmpty():
            item = self.q[self.front]
            self.front += 1
            if self.front > self.rear:
                self.clear()
            print("** " + str(item) + " removed from queue. **")
        else:
            print("** Queue is empty to dequeue **")
    def printAll(self):
        if self.isEmpty():
            print("** Queue is empty to print. **")
            return
        for i in range(self.front, self.rear+1):
            print(self.q[i])
    def clear(self):
        self.front = -1
        self.rear = -1

q = None

while True:
    os.system('cls')
    print("1. Create queue")
    print("2. Enqueue")
    print("3. Dequeue")
    print("4. Peek")
    print("5. Check queue is Empty")
    print("6. Check queue is Full")
    print("7. Print queue")
    print("8. Clear queue")
    print("9. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        if q != None:
            print("Queue already been created.")
        else:
            size = int(input("Enter the size of queue: "))
            q = Queue(size)
            print("** Queue created. **")
    elif choice == 2:
        val = input("Enter value to insert: ")
        q.enqueue(val)
    elif choice == 3:
        q.dequeue()
    elif choice == 4:
        q.peek()
    elif choice == 5:
        g = "" if q.isEmpty() else "not "
        print("Queue is " + g + "empty.")
    elif choice == 6:
        g = "" if q.isFull() else "not "
        print("Queue is " + g + "full.")
    elif choice == 7:
        print("Printing Queue: ")
        q.printAll()
    elif choice == 8:
        print("Clearing queue.")
        q.clear()
        q.q.clear()
    elif choice == 9:
        print("Exiting..")
        break
    else:
        print("Invalid choice.")

    getch = input("Press enter to continue.")

        

