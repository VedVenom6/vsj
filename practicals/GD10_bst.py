# GD10: Binary Search Tree - insert, delete, search, display (inorder/preorder/postorder)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    else:
        print("Duplicate key ignored")
    return root


def search(root, key):
    while root:
        if key == root.data:
            return True
        root = root.left if key < root.data else root.right
    return False


def min_node(root):
    while root.left:
        root = root.left
    return root


def delete(root, key):
    if root is None:
        print("Key not found")
        return None
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:              # case 1 & 2: no child / only right child
            return root.right
        if root.right is None:             # case 2: only left child
            return root.left
        succ = min_node(root.right)        # case 3: two children -> inorder successor
        root.data = succ.data
        root.right = delete(root.right, succ.data)
    return root


def inorder(root):                         # gives sorted order
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = None

while True:
    print("\n1.Insert  2.Delete  3.Search  4.Display  5.Exit")
    ch = int(input("Choice: "))
    if ch == 1:
        for k in map(int, input("Keys separated by space: ").split()):
            root = insert(root, k)
    elif ch == 2:
        root = delete(root, int(input("Key to delete: ")))
    elif ch == 3:
        print("Found" if search(root, int(input("Key to search: "))) else "Not found")
    elif ch == 4:
        if root is None:
            print("Tree is empty")
            continue
        print("Inorder  : ", end=""); inorder(root); print()
        print("Preorder : ", end=""); preorder(root); print()
        print("Postorder: ", end=""); postorder(root); print()
    elif ch == 5:
        break
    else:
        print("Invalid choice")
