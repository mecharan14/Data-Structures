import os
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    def insert(self, val):
        new = Node(val)
        if self.root == None:
            self.root = new
            print("{} inserted into BST.".format(val))
        else:
            tmp = self.root
            while tmp != None:
                if tmp.val > val:
                    if tmp.left == None:
                        tmp.left = new
                        print("{} inserted into BST.".format(val))
                        break
                    else:
                        tmp = tmp.left
                elif tmp.val < val:
                    if tmp.right == None:
                        tmp.right = new
                        print("{} inserted into BST.".format(val))
                        break
                    else:
                        tmp = tmp.right
                else:
                    print("Element already inserted.")
                    break
    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)
    def preorder(self, root):
        if root != None:
            print(root.val)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val)
    def search(self, val, root):
        if root == None:
            print("{} not found in BST".format(val))
            return
        if val < root.val:
            self.search(val, root.left)
        elif val > root.val:
            self.search(val, root.right)
        else:
            print("{} is found".format(val))
            


tree = None

while True:
    os.system("cls")
    print("1. Create a BST")
    print("2. Insert node")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice number: "))
    except:
        continue

    if choice == 1:
        if tree == None:
            tree = BST()
            print("Tree is created.")
        else:
            print("Tree already been created.")
    elif choice == 2:
        data = int(input("Enter value to insert: "))
        while data == "":
            data = input("Please enter value to insert: ")
        tree.insert(data)
    elif choice == 3:
        val = int(input("Enter value to search: "))
        while val == "":
            val = input("Enter value to search: ")
        tree.search(val, tree.root)
    elif choice == 4:
        print("Printing inorder: ")
        tree.inorder(tree.root)
    elif choice == 5:
        print("Printing preorder: ")
        tree.preorder(tree.root)
    elif choice == 6:
        print("Printing postorder: ")
        tree.postorder(tree.root)
    elif choice == 7:
        print("Exiting..")
        break
    else:
        print("Invalid choice")

    getch = input("Press enter to continue...")