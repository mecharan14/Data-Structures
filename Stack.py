import os

class Stack:
    def __init__(self, max):
        self.max = max
        self.stack = []
        self.top = -1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.max-1
    def push(self, data):
        if not self.isFull():
            self.top += 1
            self.stack.insert(self.top, data)
            print("Element pushed to stack.")
        else:
            print("Stack is full.")
    def pop(self):
        if not self.isEmpty():
            print("Element popped: "+ str(self.stack[self.top]))
            self.stack.pop()
            self.top -= 1
        else:
            print("Stack is empty.")
    def printAll(self):
        if self.isEmpty():
            print("Stack is empty to print.")
            return
        print("Printing Stack: ")
        for i in range(self.top+1):
            print(self.stack[i])

st = None

while True:
    os.system("cls")
    print("1. Create Stack")
    print("2. Push")
    print("3. Pop")
    print("4. Print Stack")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if st != None:
            print("Stack already created.")
        else:
            size = int(input("Enter the size of stack: "))
            st = Stack(size)
            print("Stack created.")
    elif choice == 2:
        val = input("Enter data to be pushed: ")
        while val == "":
            val = input("Please enter data to be pushed: ")
        st.push(val)
    elif choice == 3:
        st.pop()
    elif choice == 4:
        st.printAll()
    elif choice ==5:
        break
    else:
        print("Invalid choice")

    getch = input("Press enter to continue...")