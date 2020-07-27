import os

class Node:
    def __init__(self, n):
        self.n = n
        self.nxt = None
    def getn(self):
        print(self.n)

class List:
    def __init__(self):
        self.head = None
    def addBack(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            tmp = self.head
            while tmp.nxt != None:
                tmp = tmp.nxt
            tmp.nxt = new
    def addFront(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            new.nxt = self.head
            self.head = new
    def addByPos(self, data, pos):
        new = Node(data)
        if self.head == None:
            self.head = new
        else:
            tmp = self.head
            i = 0
            while i < pos-2 and tmp.nxt != None:
                tmp =  tmp.nxt
            new.nxt = tmp.nxt
            tmp.nxt = new
    def printAll(self):
        tmp = self.head
        if tmp == None:
            print("Empty list")
            return
        while tmp.nxt != None:
            print(tmp.n)
            tmp = tmp.nxt
        print(tmp.n)
    def delByValue(self, data):
        tmp = self.head
        while tmp.nxt != None and tmp.nxt.n != data:
            tmp = tmp.nxt
        nxtNode = tmp.nxt.nxt
        del tmp.nxt
        tmp.nxt = nxtNode
    def delByPos(self, pos):
        tmp = self.head
        i = 0
        while i < pos-2 and tmp.nxt != None:
            tmp = tmp.nxt
        nxtNode = tmp.nxt.nxt
        del tmp.nxt
        tmp.nxt = nxtNode
    def delFront(self):
        if self.head != None:
            tmp = self.head.nxt
            del self.head
            self.head = tmp
    def delBack(self):
        if self.head != None:
            tu = self.head
            while tu.nxt.nxt != None:
                tu = tu.nxt
            del tu.nxt
            tu.nxt = None

linked_list = None

while True:
    os.system('cls')
    print("1. Create Linked List")
    print("2. Add node to back")
    print("3. Add node at front")
    print("4. Add node by position")
    print("5. Delete node from back")
    print("6. Delete node at front")
    print("7. Delete node by postion")
    print("8. Delete node by value")
    print("9. Print Linked List")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if linked_list != None:
            print("Linked List already been created")
        else:
            linked_list = List()
            print("Linked List created")
    elif choice >= 2 and choice <= 4:
        data = input("Enter the value of node: ")
        while data == "":
            data = input("Please enter the value of node: ")
        if choice == 2:
            linked_list.addBack(data)
        elif choice == 3:
            linked_list.addFront(data)
        elif choice == 4:
            pos = int(input("Enter position: "))
            linked_list.addByPos(data, pos)
        print("Node Added")
    elif choice >=5 and choice <= 8:
        if choice == 5:
            linked_list.delBack()
        elif choice == 6:
            linked_list.delFront()
        elif choice == 7:
            pos = int(input("Enter position: "))
            linked_list.delByPos(pos)
        elif choice == 8:
            val = input("Enter node value: ")
            linked_list.delByValue(val)
        print("Node deleted")
    elif choice == 9:
        print("Printing Linked List:")
        linked_list.printAll()
    elif choice == 10:
        print("Exiting..")
        break
    else:
        print("Invalid choice")
    getch = input("Press enter to continue")